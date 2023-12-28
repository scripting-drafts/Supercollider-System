from math import pi
# from os import times
from subprocess import getoutput
from sc3.all import *
from sc3.synth.ugen import *
from sc3.base.builtins import reciprocal, dbamp, clip
# from sc3.synth.ugens.trig import clip
from sc3.all import SinOsc, EnvGen, Out, Mix, LPF18, LPF, LFSaw, Lag3, \
    PinkNoise, Integrator, Dust, LFNoise1, DynKlank, DetectSilence, Line

class Server_MGMT:
    '''
    Server: '127.0.0.1:57110'
    OSC Interface: '127.0.0.1:57120'
    # TODO: rewrite 
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
        # def wobble(freq=440, amp=0, gate=1, a = 0.01, d = 0.3, s = 0.5, r = 1, phase = 0.):
        #     env = EnvGen(Env.adsr(a, d, s, r), gate, done_action=0)
        #     waves = SinOsc.ar(freq, phase=pi) * amp
        #     LPF_control = SinOsc.kr(freq * 10, phase=pi) * amp
        #     LPF_control_2 = SinOsc.kr(36.71/2, phase=phase) * amp
        #     LPF_control_3 = LFSaw.kr(36.71/2) * amp
        #     sig = LPF18(waves, LPF_control_3, 1, 180)    # last 90
        #     Out([0, 1], sig * env)
        #     ...

        #     # asd = LPF18.ar(SinOsc.ar(freq=293.6, phase=pi), SinOsc.kr(freq=293.6, phase=pi), 90)
            
        # # vars = [Out.ar([0, 1], LPF18.ar(SinOsc.ar(freq=293.6, phase=pi), SinOsc.kr(freq=293.6, phase=pi), 90))]
        # sd = SynthDef('wobble', wobble)
        # sd.add()

        # @synthdef
        def mybell(freq=440, amp=1, gate=1, a = 0.01, d = 0.3, s = 0.5, r = 1, phase = 0.):
            lag=10
            i_doneAction=0
            env = EnvGen(Env.adsr(a, d, s, r), gate, done_action=i_doneAction)
            decayscale=1
            # t_trig=1
            sing_switch=0
            freqscale = freq / 2434
            # freqscale = Lag3.kr(freqscale, lag)
            # decayscale = Lag3.kr(decayscale, lag)
            
            # sing = 
            sing_switch = clip(sing_switch, str(0), str(1))
            
            input = sing_switch * LPF.ar(
                    LPF.ar(PinkNoise.ar() * Integrator.kr(sing_switch * 0.001, 0.999).linexp(0, 1, 0.01, 1) * amp,
                2434 * freqscale) + Dust.ar(0.1),
            10000 * freqscale) * dbamp(LFNoise1.kr(0.5).range(-45, -30))

            frequencies = [
                (LFNoise1.kr(0.5).range(2424, 2444)) + Line.kr(20, 0, 0.5),
                (LFNoise1.kr(0.5).range(2424, 2444)) + Line.kr(20, 0, 0.5) + LFNoise1.kr(0.5).range(1,3),
                LFNoise1.kr(1.5).range(5435, 5440) - Line.kr(35, 0, 1),
                LFNoise1.kr(1.5).range(5480, 5485) - Line.kr(10, 0, 0.5),
                LFNoise1.kr(2).range(8435, 8445) + Line.kr(15, 0, 0.05),
                LFNoise1.kr(2).range(8665, 8670),
                LFNoise1.kr(2).range(8704, 8709),
                LFNoise1.kr(2).range(8807, 8817),
                LFNoise1.kr(2).range(9570, 9607),
                LFNoise1.kr(2).range(10567, 10572) - Line.kr(20, 0, 0.05),
                LFNoise1.kr(2).range(10627, 10636) + Line.kr(35, 0, 0.05),
                LFNoise1.kr(2).range(14689, 14697) - Line.kr(10, 0, 0.05)
                ]
            
            amplitudes = [
                dbamp(LFNoise1.kr(1).range(-10, -5)),
                dbamp(LFNoise1.kr(1).range(-20, -10)),
                dbamp(LFNoise1.kr(1).range(-12, -6)),
                dbamp(LFNoise1.kr(1).range(-12, -6)),
                dbamp(-20),
                dbamp(-20),
                dbamp(-20),
                dbamp(-25),
                dbamp(-10),
                dbamp(-20),
                dbamp(-20),
                dbamp(-25)
                ]
            
            ringtimes = [
                20 * freqscale.pow(0.2),
                20 * freqscale.pow(0.2),
                5,
                5,
                0.6,
                0.5,
                0.3,
                0.25,
                0.4,
                0.5,
                0.4,
                0.6
                ] * pow(0.5, reciprocal(freqscale))
            

            sig = DynKlank.ar([
                frequencies,
                amplitudes,
                ringtimes], input, freqscale, 0, decayscale)
            
            # DetectSilence.ar(sig, done_action=i_doneAction)
            Out([0, 1], sig * env)
            ...

        st = SynthDef('mybell', mybell)
        st.add()

        # def test_1(freq=440, amp=1, pan=1, gate=1):
        #     ...

        # sd = SynthDef('test_1', test_1)
        # sd.add()

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
