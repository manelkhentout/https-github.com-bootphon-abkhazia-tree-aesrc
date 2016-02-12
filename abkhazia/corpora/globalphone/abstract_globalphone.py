"""Abstract preparator for the GlobalPhone corpus"""
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
# along with abkahzia. If not, see <http://www.gnu.org/licenses/>.

import os
import re
import shutil

from abkhazia.utils import list_directory, open_utf8, list_files_with_extension
from abkhazia.corpora.utils import AbstractPreparator


def strip_accolades(expr):
    """Returns 'expr' with accolade stripped, raise if no accolades"""
    if not (expr[0] == '{' and expr[-1] == '}'):
        raise RuntimeError(
            'Bad formatting for word or transcript: {0}'.format(expr))
    return expr[1:-1]


class AbstractGlobalPhonePreparator(AbstractPreparator):
    """Convert the GlobalPhone corpus to the abkhazia format

    For a new language xxx, you will need to write your own
    'specifics_xxx.py' and 'phoneset_xxx.py' modules in
    abkhazia.corpora.globalphones and add the language to the
    'supported_languages' list below

    """
    name = 'GlobalPhone'

    audio_format = 'shn'

    language = NotImplemented
    """the language for which the preparator is specilized for"""

    transcription_key = NotImplemented
    """the language dependant extention of transcription files"""

    exclude_wavs = []
    """a list (possibly empty) of wav files to ignore"""

    def __init__(self, input_dir, output_dir=None, verbose=False, njobs=1):
        # call the AbstractPreparator __init__
        super(AbstractGlobalPhonePreparator, self).__init__(
            input_dir, output_dir, verbose, njobs)

        self.transcription_dir = os.path.join(
            self.input_dir, 'GlobalPhone-{0}/{0}/{1}'
            .format(self.language, self.transcription_key))

        self.dictionary = os.path.join(
            self.input_dir,
            'GlobalPhoneDict-{}'.format(self.language),
            '{}-GPDict.txt'.format(self.language))

        # init language specificities
        self._erase_dict = self.correct_dictionary()
        self._erase_trs = self.correct_transcription()

    def correct_transcription(self):
        """TODO"""
        return False

    def correct_dictionary(self):
        """TODO"""
        return False

    def __del__(self):
        try:
            # the corpus correction possibly create temporary files that
            # we delete here
            if self._erase_dict:
                self.log.debug('removing corrected dictionay: {}'
                               .format(self.dictionary))
                os.remove(self.dictionary)

            if self._erase_trs:
                self.log.debug('removing corrected transcriptions: {}'
                               .format(self.transcription_dir))
                shutil.rmtree(self.transcription_dir)
        except AttributeError:
            pass

    def list_audio_files(self):
        # for some languages, there are corrupted wavefiles that we
        # need to exclude from preparation
        self.log.info('{} audio files excluded'.format(len(self.exclude_wavs)))

        # src_dir is the 'adc' directory from the GlobalPhone
        # distribution of the language considered
        src_dir = os.path.join(
            self.input_dir, 'GlobalPhone-{0}/{0}/adc'.format(self.language))

        shns = [f for f in
                list_files_with_extension(src_dir, '.adc.shn', abspath=True)
                if os.path.basename(f).replace('.adc.shn', '')
                not in self.exclude_wavs]

        wavs = [os.path.basename(shn).replace('.adc.shn', '.wav')
                for shn in shns]

        return shns, wavs

    def make_segment(self):
        with open_utf8(self.segments_file, 'w') as out:
            for wav in list_files_with_extension(self.wavs_dir, 'wav'):
                wav = os.path.basename(wav)
                out.write(u'{} {}\n'.format(wav.replace('.wav', ''), wav))

    def make_speaker(self):
        with open_utf8(self.speaker_file, 'w') as out:
            for wav in list_files_with_extension(self.wavs_dir, 'wav'):
                wav = os.path.basename(wav)
                out.write(u'{} {}\n'.format(wav.replace('.wav', ''), wav[:5]))

    def make_transcription(self):
        with open_utf8(self.transcription_file, 'w') as out:
            for trs in list_directory(self.transcription_dir, abspath=True):
                spk_id = os.path.splitext(os.path.basename(trs))[0]
                lines = open_utf8(trs, 'r').readlines()

                # add utterence id from even lines starting at line 2
                ids = [spk_id + u'_' + re.sub(ur'\s+|:|;', u'', e)
                       for e in lines[1::2]]

                # delete linebreaks on odd lines starting at line 3
                # (this does not take into account fancy unicode
                # linebreaks), see
                # http://stackoverflow.com/questions/3219014
                trs = [re.sub(ur'\r\n?|\n', u'', e) for e in lines[2::2]]

                for i, t in zip(ids, trs):
                    out.write(u'{} {}\n'.format(i, t))

    def make_lexicon(self):
        # parse dictionary lines
        words = transcripts = []
        for line in open_utf8(self.dictionary, 'r').xreadlines():
            # suppress linebreaks (this does not take into account fancy
            # unicode linebreaks), see
            # http://stackoverflow.com/questions/3219014
            line = re.sub(ur'\r\n?|\n', u'', line).split(u' ')

            # parse word
            word = strip_accolades(line[0])
            if u'{' in word or u'}' in word:
                raise RuntimeError(
                    'Bad formatting of word {}'.format(word))
            words.append(word)

            # parse phonetic transcription
            trs = strip_accolades(u' '.join(line[1:])).split(u' ')
            transcript = []
            for phone in trs:
                if phone[0] == u'{':
                    phn = phone[1:]
                    assert phn != u'WB', trs
                elif phone[-1] == u'}':
                    phn = phone[:-1]
                    assert phn == u'WB', trs
                else:
                    phn = phone
                    assert phn != u'WB', trs

                assert not(u'{' in phn), trs
                assert not(u'}' in phn), trs
                if phn != u'WB':
                    transcript.append(phn)
            transcripts.append(u' '.join(transcript))

        # generate output file
        with open_utf8(self.lexicon_file, 'w') as out:
            for word, trs in zip(words, transcripts):
                out.write('{} {}\n'.format(word, trs))
