# coding: utf-8

# Copyright 2016 Thomas Schatz, Xuan Nga Cao, Mathieu Bernard
#
# This file is part of abkhazia: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abkhazia is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with abkhazia. If not, see <http://www.gnu.org/licenses/>.
"""Provides the Corpus class"""

import os

from abkhazia.corpus.corpus_saver import CorpusSaver
from abkhazia.corpus.corpus_loader import CorpusLoader
from abkhazia.corpus.corpus_validation import CorpusValidation
from abkhazia.corpus.corpus_split import CorpusSplit
import abkhazia.utils as utils


class Corpus(object):
    """Speech corpus in the abkhazia format

    This class wraps a speech corpus in the abkhazia format and
    provides methods/attritutes to interact with it in a consistent
    and safe way.

    TODO metainfo -> (name, creation date, source)
    TODO logging support
    TODO implement variants phones

    Attributes
    ==========

    wavs: dict(wav_id, path)
    ------------------------

    - corpus wav files
    - wav_id is usually the file basename without extension, path is
      the absolute path to the file
    - exemple: ('s01', '/path/to/wavs/s01.wav')

    lexicon: dict(word, phones)
    ---------------------------

    - dictionary of corpus words to phones
    - word and phones are both str, phones are separated by ' '
    - exemple: ('weeks', 'w iy k s')

    segments: dict(utt_id, (wav_id, tbegin, tend))
    ----------------------------------------------

    - time interval in wav files mapped to each corpus utterance
    - tbegin and tend anre None if the wav file contains a single
      utterance, else they correspond to begin and end times in the
      wav (in seconds, as float)
    - exemple: ('s01u01', ('s01', 0, 0.75))

    text: dict(utt_id, str)
    -----------------------

    - transcription associated to each corpus utterance
    - exemple: ('s01u01', 'yeah <SIL> oh yeah')

    utt2spk: dict(utt_id, spk_id)
    -----------------------------

    - corpus utterances mapped to their speaker
    - exemple: ('s01u01', 's01')

    phones: dict(str, str)
    ----------------------

    - corpus phones mapped to their IPA equivalent
    - exemple: ('iy', u'iː')

    silences: list(str)
    -------------------

    - corpus silence phones
    - exemple: ['<SIL>']

    variants: list(str)
    -------------------

    - alternative phones variants (not yet implemented)
    - exemple: []

    """

    @classmethod
    def load(cls, corpus_dir, log=utils.null_logger()):
        """Return a corpus initialized from `corpus_dir`

        Raise IOError if corpus_dir if an invalid directory, the
        output corpus is not validated.

        """
        return CorpusLoader.load(cls, corpus_dir, log=log)

    def __init__(self, log=utils.null_logger()):
        """Init an empty corpus"""
        self.log = log
        self.wavs = dict()
        self.lexicon = dict()
        self.segments = dict()
        self.text = dict()
        self.phones = dict()
        self.utt2spk = dict()
        self.silences = []
        self.variants = []

    def save(self, path, no_wavs=False):
        """Save the corpus to the directory `path`

        `path` is assumed to be a non existing directory.

        If `no_wavs` if True, dont save the wavs (ie don't write wavs
        subdir)

        """
        self.log.info('saving corpus to %s', path)
        CorpusSaver.save(self, path, no_wavs=no_wavs)

    def validate(self, njobs=utils.default_njobs()):
        """Validate speech corpus data

        Raise IOError on the first encoutered error, relies on the
        CorpusValidation class.

        """
        CorpusValidation(self, njobs=njobs, log=self.log).validate()

    def is_valid(self, njobs=utils.default_njobs()):
        """Return True if the corpus is in a valid state"""
        try:
            self.validate(njobs=njobs)
        except IOError:
            return False
        return True

    def utts(self):
        """Return the list of utterance ids stored in the corpus"""
        return self.utt2spk.keys()

    def spks(self):
        """Return the list of speaker ids stored in the corpus"""
        return self.spk2utt().keys()

    def spk2utt(self):
        """Return a dict of speakers mapped to an utterances list

        Built from self.utt2spk. This method is a Python
        implementation of the Kaldi script
        egs/wsj/s5/utils/utt2spk_to_spk2utt.pl.

        """
        # init an empty list for all speakers
        spk2utt = {spk: [] for spk in set(self.utt2spk.itervalues())}

        # populate lists with utterance ids
        for utt, spk in self.utt2spk.iteritems():
            spk2utt[spk].append(utt)
        return spk2utt

    def wav2utt(self):
        """Return a dict of wav ids mapped to utterances/timestamps they contain

        The values of the returned dict are tuples (utt-id, tstart,
        tend). Built on self.segments.

        """
        # init an empty list for all wavs
        wav2utt = {wav: [] for wav, _, _ in self.segments.itervalues()}

        # populate lists with utterance ids and timestamps
        for utt, (wav, tstart, tend) in self.segments.iteritems():
            wav2utt[wav].append((utt, float(tstart), float(tend)))
        return wav2utt

    def utt2duration(self):
        """Return a dict of utterances ids mapped to their duration

        Durations are floats expressed in second, read from wav files

        """
        utt2dur = dict()
        for utt, (wav, start, stop) in self.segments.iteritems():
            start = 0 if start is None else start
            stop = utils.wav.duration(wav) if stop is None else stop
            utt2dur[utt] = stop - start
        return utt2dur

    def words(self, in_lexicon=True):
        """Return a set of words composing the corpus

        The listed words are present in both text and lexicon (if
        `is_lexicon` is True), or in text only. The returned result is
        a set for search efficiency.

        """
        return set(
            word for utt in self.text.itervalues() for word in utt.split()
            if (word in self.lexicon if in_lexicon else True))

    def has_several_utts_per_wav(self):
        """Return True if there is several utterances in at least one wav"""
        for _, start, stop in self.segments.itervalues():
            if start is not None or stop is not None:
                return True
        return False

    def subcorpus(self, utt_ids, prune=True):
        """Return a subcorpus made of utterances in `utt_ids`

        The returned corpus is validated and pruned (except if `prune`
        is False)

        Raise a KeyError if one utterance in `utt_ids` is in the
        input corpus.

        Raise an IOError if the subcorpus is not valid (this should
        not occurs if the input corpus is valid).

        """
        corpus = Corpus()
        corpus.lexicon = self.lexicon
        corpus.phones = self.phones
        corpus.silences = self.silences
        corpus.variants = self.variants

        corpus.wavs = {k: os.path.realpath(v)
                       for k, v in self.wavs.iteritems()}

        corpus.segments = dict()
        corpus.text = dict()
        corpus.utt2spk = dict()
        for utt in utt_ids:
            corpus.segments[utt] = self.segments[utt]
            corpus.text[utt] = self.text[utt]
            corpus.utt2spk[utt] = self.utt2spk[utt]

        if prune:
            corpus.prune()
        corpus.validate()
        return corpus

    def prune(self):
        """Removes unregistered utterances from a corpus

        This method modifies the corpus in place and return None

        The pruning operation delete undesired data from utterances
        listed in self.utts(). It removes any segment, text, wav with
        an unknown utterance id. It prune the lexicon and phones from
        the pruned text.

        """
        # prune utterance indexed dicts from the utterances list
        utts = set(self.utts())
        for d in (self.segments, self.text, self.utt2spk):
            d = {key: value for key, value in d.iteritems()
                 if key in utts}

        # prune wavs from pruned segments
        wavs = set(self.wav2utt().iterkeys())
        self.wavs = {key: value for key, value in self.wavs.iteritems()
                     if key in wavs}

        # prune lexicon from pruned text
        words = self.words(in_lexicon=False)
        self.lexicon = {key: value for key, value in self.lexicon.iteritems()
                        if key in words}

        # prune phones from pruned lexicon
        phones = set(phone for phones in self.lexicon.itervalues()
                     for phone in phones.split())
        self.phones = {key: value for key, value in self.phones.iteritems()
                       if key in phones}

    def split(self, train_prop=None, test_prop=None,
              by_speakers=True, random_seed=None):
        """Split a corpus in train and testing subcorpora

        Return a pair (train, testing) of Corpus instances, validated
        and pruned.

        test_prop : float, should be between 0.0 and 1.0 and
          represent the proportion of the dataset to include in the
          test split. If None, the value is automatically set to the
          complement of the train size. If train size is also None,
          test size is set to 0.5 (default is None).

        train_prop : float, should be between 0.0 and 1.0 and
          represent the proportion of the dataset to include in the
          train split. If None, the value is automatically set to the
          complement of the test size (default is None).

        by_speakers : bool, split the corpus by speakers if True, else
          split by utterances (regardless of speakers distribution).
          Note that this might not be appropriate when the amount of
          utterances available per speaker is too unbalanced (default
          is True).

        random_seed : seed for pseudo-random numbers generation (default
          is to use the current system time)

        """
        spliter = CorpusSplit(self, random_seed=random_seed, prune=True)
        split_fun = (spliter.split if by_speakers is False
                     else spliter.split_by_speakers)
        return split_fun(train_prop, test_prop)
