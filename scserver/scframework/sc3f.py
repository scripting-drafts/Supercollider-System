from math import pi
# from os import times
from subprocess import getoutput
from sc3.all import *
from sc3.all import SinOsc, EnvGen, Out, Mix, LPF18, LFSaw


class Server_MGMT:
    '''
    Server: '127.0.0.1:57110'
    OSC Interface: '127.0.0.1:57120'
    '''
    def server_boot():
        # s.options.program = r'C:\Program Files\SuperCollider-3.12.2\scsynth.exe'
        s.boot()
        s.dump_tree(True)
        return s

    def server_quit(sv):
        sv.free_nodes()
        server_kill = getoutput("taskkill /IM scsynth.exe /F")
        print(server_kill)

    def free_nodes(sv):
        sv.free_nodes()

class Synths_MGMT:
    
    def set_synth():
        '''
        attack_time: float = 0.01,
        decay_time: float = 0.3,
        sustain_level: float = 0.5,
        release_time: float = 1,
        peak_level: float = 1,
        curve: float = -4,
        bias: float = 0
        '''
        def wobble(freq=440, amp=0, gate=1, a = 0.01, d = 0.3, s = 0.5, r = 1, phase = 0.):
            env = EnvGen(Env.adsr(a, d, s, r), gate, done_action=2)
            waves = SinOsc.ar(freq, phase=pi) * amp
            LPF_control = SinOsc.kr(freq * 10, phase=pi) * amp
            LPF_control_2 = SinOsc.kr(36.71/2, phase=phase) * amp
            LPF_control_3 = LFSaw.kr(36.71/2) * amp
            sig = LPF18(waves, LPF_control_3, 1, 180)    # last 90
            Out([0, 1], sig * env)
            ...

            # asd = LPF18.ar(SinOsc.ar(freq=293.6, phase=pi), SinOsc.kr(freq=293.6, phase=pi), 90)
            
        # vars = [Out.ar([0, 1], LPF18.ar(SinOsc.ar(freq=293.6, phase=pi), SinOsc.kr(freq=293.6, phase=pi), 90))]
        sd = SynthDef('wobble', wobble)
        sd.add()

        def test_1(freq=440, amp=1, pan=1, gate=1):
            ...

        sd = SynthDef('test_1', test_1)
        sd.add()

        @synthdef
        def ha_reso(freq=36.71, amp=1, gate=1):
            # env = EnvGen(Env.adsr(), gate, done_action=2)
            harmonics = [2, 4, 6, 8, 10]
            # amp = amp / len(harmonics)
            # base_sigs = [SinOsc(freq * h, phase=pi) * amp for h in harmonics]
            # sig = Mix.new(base_sigs)
            # Out(0, (sig * env).dup())
            
        @synthdef
        def sine(freq=440, amp=1, gate=1):
            sig = SinOsc(freq) * amp
            env = EnvGen(Env.adsr(), gate, done_action=2)
            Out(0, (sig * env).dup())

        @synthdef
        def reso(freq=293.6, amp=1, gate=1):
            '''
            Next steps:
             - Additive SinOsc's mix
             - Set a cyclic Env to the LFP'''
            # freq = 36.71    # / 20000
            # LPF18.ar(SinOsc.ar(293.6, pi, 0.7, 0), SinOsc.kr(293.6, pi, 0.7, 0), 90)
            # source_audio = LFSaw(freq, iphase=pi) * amp
            # LPF_control = LFSaw.kr(freq, iphase=pi) * amp
            # harmonics = [1, 2, 4, 6, 8, 10]
            # freq = [x for x in range(0., freq, 0.1)]

            

            # f = {
            #     "low_cut_LOW" : freq[0],
            #     "high_cut_LOW" :freq[80],

            #     "low_cut_MEDIUM_low" : freq[120],
            #     "mid_cut_MEDIUM" : freq[300],
            #     "high_cut_MEDIUM" : freq[600],

            #     "low_cut_high" : freq[1200],
            #     "mid_cut_high" : freq[3000],
            #     "high_cut_high": freq[12000],

            #     "top_cut": freq[-1]
            # }

            # w = waves_shapes["sin_osc"]

            waves = SinOsc(freq, phase=pi) * amp
            LPF_control = SinOsc.kr(freq * 10, phase=pi) * amp
            sig = LPF18(waves, LPF_control, 0.9, 90)
            env = EnvGen(Env.adsr(0.01, 0.3, 1, 0.01, 1, 0.01), gate, done_action=2)
            # levels = [0.3, 0.7]
            # env = EnvGen(Env.cyclic(levels=levels, times=2), gate, done_action=2)
            Out(0, (sig * env).dup())
            # Out(0, sig.dup())

        

        sine.dump_ugens()

    # def start_synth(self, synth):
    #     synth_name = str(synth.__getattribute__("name"))
    #     synth = ThreadR(target=Synth, args=(synth_name,))
    #     synth.start()
    #     synth = synth.join()
    #     return synth
    
    # def stop_synth(self, synth):
    #     # synth = synth.join()
    #     synth_stop_thread = Thread(target=synth.release)
    #     synth_stop_thread.start()
    #     synth_stop_thread.join()
