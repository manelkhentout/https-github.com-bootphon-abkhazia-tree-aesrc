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
    def load(cls, corpus_dir):
        """Return a corpus initialized from `corpus_dir`

        Raise IOError if corpus_dir if an invalid directory, the
        output corpus is not validated.

        """
        return CorpusLoader.load(cls, corpus_dir)

    def __init__(self):
        """Init an empty corpus"""
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
        CorpusSaver.save(self, path, no_wavs=no_wavs)

    def validate(self,
                 njobs=utils.default_njobs(),
                 log=utils.log2file.null_logger()):
        """Validate speech corpus data

        Raise on the first encoutered error, relies on the
        CorpusValidation class.

        """
        CorpusValidation(
            self, njobs=njobs, log=log).validate()

    def is_valid(self, njobs=utils.default_njobs()):
        """Return True if the corpus is validated, False else"""
        try:
            self.validate()
        except:
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
        """Return a dict of utterances ids mapped to their duration (in s.)"""
        d = dict()
        for utt, (wav, start, stop) in self.segments.iteritems():
            start = 0 if start is None else start
            stop = utils.wav.duration(wav) if stop is None else stop
            d[utt] = stop - start
        return d

    def words(self, in_lexicon=True):
        """Return a set of words composing the corpus

        The listed words are present in both text and lexicon (if
        `is_lexicon` is True), or in text only. The returned result is
        a set for search efficiency.

        """
        def _in(a, b):
            return a in b if in_lexicon else True

        return set(word for utt in self.text.itervalues()
                   for word in utt.split() if _in(word, self.lexicon))

    def has_several_utts_per_wav(self):
        """Return True if there is several utterances in at least one wav"""
        for _, start, stop in self.segments.itervalues():
            if start is not None or stop is not None:
                return True
        return False

    def subcorpus(self, utt_ids, prune=True):
        """Return a subcorpus made of utterances in `utt_ids`

        Each utterance in `utt_ids` is assumed to be part of self,
        else a KeyError is raised.

        Raise if the subcorpus is not valid.

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
        """Removes unregistered utterances from a corpus"""
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
              by_speakers=True, prune=True, random_seed=None):
        spliter = CorpusSplit(self, random_seed=random_seed, prune=prune)
        split_fun = (spliter.split if by_speakers is False
                     else spliter.split_by_speakers)
        return split_fun(train_prop, test_prop)
