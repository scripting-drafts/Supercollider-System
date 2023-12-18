from time import sleep
from sc3.all import Synth, LFSaw, Osc, SinOsc, SyncSaw   #, synthdef, SinOsc, EnvGen, Env, Out
from tools import ThreadS
from sc3.synth.server import Server

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

# waves_shapes = {
#     "LFSaw": LFSaw(),
#     "pure_wave": Osc(),
#     "sin_osc": SinOSC(),
#     "sync_saw": SyncSaw()
# }

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

sleep(1)

#################### Ascencion
freq=36.71
# harmonics = [2, 4, 6, 8, 10, 12, 14]
# synths = [ThreadS(target=Synth, args=('new_paused', 'ha_reso', freq*h, 1/len(harmonics))) for h in harmonics]
# [t.start() for t in synths]
# synths = [t.join() for t in synths]

# sleep(1)
# [n.release() for n in synths]



t = ThreadS(target=Synth.new_paused, args=('test', 440*3, 1))
t.start()
t = t.join()
# message = t.get('12', 'test')
# print(message)
sleep(1)
t.release()

r = Server.free_all('127.0.0.1:57110')

# Synth('ha_reso', freq, None, add_action='addToHead', register=True)




# n.release()
# synths = Synths_MGMT()
# synth_name = synths.set_synth()
# synth = synths.start_synth(synth_name)

# synths.stop_synth(synth)