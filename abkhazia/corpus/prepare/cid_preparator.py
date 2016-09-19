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
"""Data preparation for the CID corpus"""

import os
import sys

import abkhazia.utils as utils
from abkhazia.corpus.prepare import AbstractPreparator


class CIDPreparator(AbstractPreparator):
    """Convert the CID corpus to the abkhazia format"""

    name = 'cid'
    description = 'Corpus of Interactional Data'

    long_description = '''8 French dialogues involving 2 participants, with the following data:
    - a wav file for each speaker
    - the inter-pausals units (IPU) annotation aligned with audio signal
    - enriched orthographic transcription (TOE) aligned with audio signal
    - phones aligned with audio signal
    - syllables aligned with audio signal
    - tokens aligned with audio signal
    - syntax aligned with the signal at the level of tokens
    '''

    url = 'http://sldr.org/sldr000720'
    audio_format = 'wav'

    # IPA transcriptions for all phones in the CID corpus. 
    phones = {
        '@': u'ə',
        'a~': u'ɑ̃',
        'A': u'a',
        'b': u'b',
        'd': u'd',
        'e': u'e',
        'f': u'f',
        'g': u'g',
        'H': u'ɥ',
        'i': u'i',
        'j': u'j',
        'k': u'k',
        'l': u'l',
        'm': u'm',
        'n': u'n',
        'o~': u'ɔ̃',
        'o': u'o',
        'p': u'p',
        'R': u'ʁ',
        's': u's',
        'S': u'ʃ',
        't': u't',
        'u': u'u',
        'U~': u'ɛ̃',
        'v': u'v',
        'w': u'w',
        'y': u'y',
        'z': u'z',
        'Z': u'ʒ',

    }

    silences = [u"SIL_WW", u"NSN"]  # SPN and SIL will be added automatically

    variants = []  # could use lexical stress variants...

    def __init__(self, input_dir, log=utils.logger.null_logger(),
                 copy_wavs=False):
        super(CIDPreparator, self).__init__(input_dir, log=log)
        self.copy_wavs = copy_wavs

    def _yield_transcription(self, trs_file):
        """Yield (utt, wav, text, tstart, tstop) read from transcription"""
        # speaker id are the first 2 letters of the file
        spk = os.path.basename(trs_file)[:2]

        utt, tstart, tstop, text = None, None, None, None
        for line in (l.strip() for l in utils.open_utf8(trs_file, 'r')):
            if line.startswith('intervals ['):
                utt = spk + '_' + line.split('[')[1][:-2]
                tstart, tstop = None, None
            elif line.startswith('xmin'):
                tstart = float(line.split(' = ')[1])
            elif line.startswith('xmax'):
                tstop = float(line.split(' = ')[1])
            elif line.startswith('text'):
                text = line.split(' = ')[1]

            if utt and tstart and tstop:
                yield utt, spk + '-anonym', text, tstart, tstop
                utt, tstart, tstop, text = None, None, None, None

    def list_audio_files(self):
        return utils.list_files_with_extension(
            os.path.join(self.input_dir, 'wav'), '.wav', abspath=True)

    def make_segment(self):
        segments = dict()

        # transcription files are CID/TextGrid/*transcription*.TextGrid
        trs_files = (t for t in utils.list_directory(
            os.path.join(self.input_dir, 'TextGrid'), abspath=True)
                     if 'transcription' in os.path.basename(t))
        for trs_file in trs_files:
            for utt, wav, _, tstart, tstop in self._yield_transcription(trs_file):
                segments[utt] = (wav, tstart, tstop)
        return segments

    def make_speaker(self):
        return {k: k[:2] for k in self.make_segment().iterkeys()}

    def make_transcription(self):
        pass
        # text = dict()
        # for utts in self._list_files('.txt', exclude=['readme']):
        #     bname = os.path.basename(utts)
        #     utt = os.path.splitext(bname)[0]
        #     for idx, line in enumerate(
        #             (l.strip() for l in open(utts).readlines()
        #              if len(l.strip())), start=1):
        #         text[utt + '-sent' + str(idx)] = line

        # # one utterance have "k p's" in text, where "k p" is an
        # # acronym in this context. Because "p's" is processed as OOV, we
        # # simply replace it by "p"
        # text['s2202b-sent15'] = text['s2202b-sent15'].replace("p's", "p")
        # return text

    def make_lexicon(self):
        # Retrieve utterances
        yield_transcription(self, trs_file)



        pass
        # dict_word = dict()
        # no_trs = set()
        # for utts in self._list_files('.words_fold'):
        #     for line in open(utts, 'r').readlines():
        #         format_match = re.match(
        #             r'\s\s+(.*)\s+(121|122)\s(.*)', line)

        #         if format_match:
        #             word_trs = format_match.group(3)
        #             word_format_match = re.match(
        #                 "(.*); (.*); (.*); (.*)", word_trs)

        #             if word_format_match:
        #                 word = word_format_match.group(1)
        #                 phn_trs = word_format_match.group(3)
        #                 if phn_trs == '':
        #                     no_trs.add(word)
        #                 else:
        #                     dict_word[word] = phn_trs

        # really_no_trs = [t for t in no_trs if t not in dict_word]
        # if really_no_trs:
        #     self.log.debug(
        #         'following words have no transcription in lexicon: {}'
        #         .format(really_no_trs))
        # return dict_word