# Copyright 2016 Thomas Schatz, Xuan-Nga Cao, Mathieu Bernard
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
"""Provides the CorpusSplitLibrivox class"""

import ConfigParser
import random
import os
from collections import defaultdict
from abkhazia.utils import logger, config, open_utf8


class CorpusSplitLibrivox(object):
    """A class for spliting an abkhazia/Librivox corpus into train and test subsets

    corpus : The abkhazia corpus to split. The corpus is assumed
      to be valid.

    log : a logging.Logger instance to send log messages

    random_seed : Seed for pseudo-random numbers generation (default
      is to use the current system time)

    prune : If True the train and testing corpora are pruned (default is True)

    In the split and split_by_speakers methods, arguments are as follow:

        test_prop : float, should be between 0.0 and 1.0 and
          represent the proportion of the dataset to include in the
          test split. If None, the value is automatically set to the
          complement of the train size. If train size is also None,
          test size is set to 0.5. (default is None)

        train_prop : float, should be between 0.0 and 1.0 and
          represent the proportion of the dataset to include in the
          train split. If None, the value is automatically set to the
          complement of the test size. (default is None)


    """
    def __init__(self, corpus, log=logger.null_logger(),
                 random_seed=None, prune=True):
        self.log = log
        self.prune = prune
        self.corpus = corpus

        # seed the random generator
        if random_seed is not None:
            self.log.debug('random seed is %i', random_seed)
        random.seed(random_seed)

        # read utt2spk from the input corpus
        utt_ids, utt_speakers = zip(*self.corpus.utt2spk.iteritems())
        self.utts = zip(utt_ids, utt_speakers)
        self.size = len(utt_ids)
        self.speakers = set(utt_speakers)
        self.log.debug('loaded %i utterances from %i speakers',
                       self.size, len(self.speakers))


    def splitLibrivox(self,out_path):
        """Split the corpus by utterances regardless of the speakers

        Both generated subsets get speech from all the speakers with a
        number of utterances by speaker in each set matching the
        number of utterances by speaker in the whole corpus.

        Return a pair (train, testing) of Corpus instances

        """
        utt2dur=self.corpus.utt2duration()
        utts=self.utts
        speakers=self.speakers
        spk2utts=dict()
        spk2dur=dict()

        #train=self.read_text_files(in_path)
        train_utt_ids=[]
        test_utt_ids=[]
        family=[]
        new_speakers=[]

        for utt,spkr in utts:
            utt_list=utt.split('_')
            type_spkr=utt_list[3]
            train_test=utt_list[4]
            
            #Split between train or test
            if train_test=='tr': 
                train_utt_ids.append(utt)
            elif train_test=='te':
                test_utt_ids.append(utt)
            else : 
                print "neither train or test : check",utt
            
            #Write family/new speakers text files
            if type_spkr=='L':
                family.append(spkr)
            elif type_spkr=='N':
                new_speakers.append(spkr)
                
        #write new speakers and family speakers lists
        self.write_text(family,os.path.join(out_path,'family/family.txt'))
        self.write_text(new_speakers,os.path.join(out_path,'new_speakers/new_speakers.txt'))

        return (self.corpus.subcorpus(train_utt_ids, prune=self.prune),
                self.corpus.subcorpus(test_utt_ids, prune=self.prune))

    def read_text_files(self,in_path):
        train=[]
        with open(in_path,'r') as fin:
            train_files=fin.readlines()
            for line in train_files:
                train.append(line.strip('\n'))
        return(train)
    
    def write_text(self,alist,name):
        
        if not os.path.isdir(os.path.dirname(name)):
            os.makedirs(os.path.dirname(name))
        alist=list(set(alist))
        with open_utf8(name,'w') as fout:
            for line in alist:
                fout.write(u'{}\n'.format(line))



        