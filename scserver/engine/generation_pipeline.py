# from debugger import Logger
import random
from .samples_engine import SamplesLibGenerate
import numpy as np

class SamplesData:
    def __init__(self, seed=50):
        '''
        120 bpm -> 0.5s per beat | 8s per bar (16 * .5)
        60 bpm -> 1s per beat | 16s per bar (16 * 1)
        ~ 140 bpm -> 0.42857142857s per beat | 6.85714285714s per bar (16 * 0.42857142857)
        '''
        # self.logger = Logger().logging()
        self.generate = SamplesLibGenerate()
        # random.seed(seed)

        self.bpm = 190  # 60 # 130
        self.time_signature = 4

        self.bars = 16
        self.bars_len = float(self.bpm / self.bars / self.time_signature)
        self.notes = self.generate.get_notes() + self.generate.get_notes()
        self.chosen_notes = self.notes

        # fast_notes = [x for x in np.arange(self.bars_len/24., self.bars_len/1)] # range = [float(x) + 0.005 + bias for x in zip(np.arange(self.bars_len/24., self.bars_len/1), np.arange(0.005, .5]
        fast_notes = [float(x) + bias for x, bias in zip(np.arange(self.bars_len/24., self.bars_len/1), np.arange(0.005, 1., .0005))]
        # self.notes_len = [random.choice(np.arange(self.bars_len/, 60/self.bpm)).item()
        #                    for _ in self.chosen_notes],

        self.notes_len = [random.choice(fast_notes) for _ in self.chosen_notes]
        self.time_left = [self.bpm/self.bars - x for x in self.notes_len]
        self.swing = random.choice(np.arange(0, self.bpm / 7000, self.bpm / 6996)).item()
        
        # self.logger.debug('chosen_notes: %s' % self.chosen_notes)
        # self.logger.debug('notes_len %s' % self.notes_len)
        # self.logger.debug('time_left %s' % self.time_left)