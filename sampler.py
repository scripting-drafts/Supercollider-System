from sc3.synth.server import Server
from time import sleep
from scserver.engine import Logger, SamplesLib
import numpy as np
from sc3.all import Synth
from sc3.base.builtins import midicps
from math import pi
import sys

class Sampler:
    def __init__(self):
        self.logger = Logger().logging()
        self.s_func()
        self.phases = np.arange(-pi*2, pi*2, 0.1)
        self.phases.tolist() 
    
    def s_func(self):
        self.t = Synth('wobble', None, None)
        sleep(2)
    
    def i_func(self, t, freq=440, amp=1, gate=1, a = 0.01, d = 0.3, s = 0.5, r = 1, phase = pi):
        self.t.set(freq, amp, gate, a, d, s, r, phase)
                
    def play_source(self, sample_attrs):
        for r in range(16):
            try:
                bar_left = sample_attrs['bars_len'] / sample_attrs['time_signature']
                # note_threads = []

                for midi_note, note_len, time_left in zip(sample_attrs['notes'],
                                                                   sample_attrs['notes_len'],
                                                                   sample_attrs['time_left']):
                    
                    
                    if midi_note is not None:
                        midi_note = int(midicps(midi_note))
                        self.i_func(self.t, freq=midi_note, amp=1, gate=1)
                                    # a=self.a_choice(), d=self.float_choice(), s=self.a_choice(), r=self.float_choice(), phase=self.get_phase())

                        self.logger.debug(f'Bars number: {r}')
                        self.logger.debug(f'Note: {midi_note}', )
                        self.logger.debug(f'Note length: {note_len}')                        

                        bar_left = bar_left - note_len if bar_left > 0 else bar_left
                        self.logger.debug(f'Bar left: {bar_left}')

                        if not bar_left < 0:
                            sleep(bar_left)
                        else:
                            self.logger.debug(f'{bar_left} is negative')
                            bar_left = sample_attrs['bars_len'] / sample_attrs['time_signature']
                    else:
                        if not bar_left < 0:
                            sleep(bar_left)
                        
                        bar_left = sample_attrs['bars_len'] / sample_attrs['time_signature']

                    self.i_func(self.t, freq=midi_note, amp=0, gate=1)

            except KeyboardInterrupt:
                r = Server.free_all('127.0.0.1:57110')
                sys.exit()

    def int_choice(self):
        n = int(np.random.choice([0, 1], 1, [.2, .8])[0])

        return n

    def float_choice(self):
        n = float(np.random.choice([0., 1.], 1, [.2, .8])[0])

        return n

    def a_choice(self):
        n = float(np.random.choice([0.1, 1.], 1, [.7, .3])[0])

        return n
    
    def get_phase(self):
        phase = float(np.random.choice(self.phases, 1, [.2, .8])[0])

        return phase

    def play_note(self, midi_note, note_len):
        note_on = [0x90, midi_note, 112]
        note_off = [0x80, midi_note, 0]
        self.midiout.send_message(note_on)
        sleep(note_len)
        self.midiout.send_message(note_off)

        return       

    def play_sample(self, sample_attrs, times=None):
        for _ in range(times):
            for sample in sample_attrs['samples']:
                try:
                    note_length, time_left = sample_attrs['bars_time'][sample_attrs['samples'].index(sample)]
                    if note_length is not None:
                        sleep(sample_attrs['swing'])
                        note_on = [0x90, sample, 112]
                        note_off = [0x80, sample, 0]
                        self.midiout.send_message(note_on)
                        sleep(note_length)
                        self.midiout.send_message(note_off)
                    sleep(time_left)
                
                except KeyboardInterrupt:
                    self.i_func(self.t, freq=440, amp=1, gate=0)
                    r = Server.free_all('127.0.0.1:57110')
                    exit()

    def play_16(self, sample_attrs):
        self.play_source(sample_attrs)
        self.play_sample(sample_attrs, 7)


sample = SamplesLib()
s = Sampler()
s.play_source(sample.hh)