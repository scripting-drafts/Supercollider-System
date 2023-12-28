from time import sleep
from sc3.all import Synth, LFSaw, Osc, SinOsc, SyncSaw   #, synthdef, SinOsc, EnvGen, Env, Out
# from tools import ThreadS
from sc3.synth.server import Server
import numpy as np
from math import pi
import random

# import ray

# ray.init()

waves_shapes = {
                "lf_saw": LFSaw,
                "pure_wave": Osc,
                "sin_osc": SinOsc,
                "sync_saw": SyncSaw
            }

# harmonics = [1, 2, 4, 6, 8, 10]
# # freq_eq = [np.linspace(0, 20000, 0.1), np.array(np.linspace(0, 1, 0.001))]

# freq_eq = np.zeros((20000), 0.001)
# print(freq_eq)

# freq = [x for x in range(0., freq, 0.1)]

# eq = {
#     "low_cut_LOW" : freq[0],
#     "high_cut_LOW" :freq[80],

#     "low_cut_MEDIUM_low" : freq[120] ,
#     "mid_cut_MEDIUM" : freq[300],
#     "high_cut_MEDIUM" : freq[600],

#     "low_cut_high" : freq[1200],
#     "mid_cut_high" : freq[3000],
#     "high_cut_high": freq[12000],

#     "top_cut": freq[-1]
# }

# n = [Synth('reso', f, 1 / len(freq_eq[0])) for f, e in freq_eq.tolist()]
# n.set('amp', 0.05)
# n.set('freq', 550)

#################### Ascension
freq=36.71
# harmonics = [2, 4, 6, 8, 10, 12, 14]
# synths = [ThreadS(target=Synth, args=('new_paused', 'ha_reso', freq*h, 1/len(harmonics))) for h in harmonics]
# [t.start() for t in synths]
# synths = [t.join() for t in synths]

# sleep(1)
# [n.release() for n in synths]

########## ThreadS Approach
# t = ThreadS(target=Synth.new_paused, args=('test', 440*3, 1))
# t.start()
# t = t.join()
# # message = t.get('12', 'test')
# # print(message)
# sleep(1)
# t.release()


########### RAY Approach
# @ray.remote
def s_func(freq=440, amp=1, gate=1, a = 0.01, d = 0.3, s = 0.5, r = 1, phase = 0.):

    '''[freq, amp, gate, a, d, s, r]'''
    t = Synth('mybell', None)
    # sleep(a + d + s + r)
    # t.release()
    return t

# @ray.remote
def i_func(t, freq=440, amp=1, gate=1, a = 0.01, d = 0.3, s = 0.5, r = 1, phase = pi):
    t.set(freq, amp, gate, a, d, s, r, phase)
    sleep(a + d + s + r)
    # t.release()

# s = s_func.remote(0)
# i = i_func.remote(1)

# s, i = ray.get([s, i])
    
def adsr_sum(bpm, bar_len, pre_bar, bar_left):
    
    return
    
def int_choice():
    n = int(np.random.choice([0, 1], 1, [.1, .9])[0])

    return n

def float_choice():
    n = float(np.random.choice([0., 1.], 1, [.2, .8])[0])

    return n

def a_choice():
    n = float(np.random.choice([0.1, 1.], 1, [.7, .3])[0])

    return n

phases = np.arange(-pi*2, pi*2, 0.1)
phases.tolist()

def get_phase():
    phase = float(np.random.choice(phases, 1, [.2, .8])[0])

    return phase
    

t = s_func()
sleep(200)

# ### TEST
# try:
#     t = s_func()
#     sleep(3)

#     while True:
#         i_func(t, freq=739, amp=float_choice(), gate=int_choice(), a=a_choice(), d=float_choice(), s=a_choice(), r=float_choice(), phase=get_phase())

# except KeyboardInterrupt:
#     t.release()
    
# a = 0.01
# d = 0.3
# s = 0.5
# r = 0.1

# bpm = 140




# while True:
#     try:
#         i_func(t, freq=440, amp = choice_def(), gate = choice_def(), a = 0.01, d = 0.3, s = 0.5, r = 0.1)

#     except KeyboardInterrupt:
#         t.release()
#         break

# sleep(5)
# i_func(1)
# DEBUG
# t = Synth('test', 440*3, 1)
# sleep(1)
# t.release()

r = Server.free_all('127.0.0.1:57110')

# Synth('ha_reso', freq, None, add_action='addToHead', register=True)




# n.release()
# synths = Synths_MGMT()
# synth_name = synths.set_synth()
# synth = synths.start_synth(synth_name)

# synths.stop_synth(synth)