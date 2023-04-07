#IMPORTS
import numpy as np
#from scipy.io import wavfile
#from multipledispatch import dispatch
import sounds

def piano(*args):

    if len(args) == 1 and type(args[0]) == int:    # more argument types to be considered later
        frequency = 2 ** ((args[0] - 49)/12) * 440

    return frequency

wave1 = sounds.wave(piano(40), 100, 0.2)
wave2 = sounds.wave(piano(44), 100, 0.2)
wave3 = sounds.wave(piano(45), 100, 0.4)
wave45 = sounds.wave(100, 0, 0.05)
wave4 = sounds.wave(piano(45), 100, 0.4)
wave5 = sounds.wave(piano(45), 100, 0.2)
wave6 = sounds.wave(piano(47), 100, 0.2)
wave7 = sounds.wave(piano(49), 100, 0.4)
wave75 = sounds.wave(100, 0, 0.05)
wave8 = sounds.wave(piano(49), 100, 0.4)
wave85 = sounds.wave(100, 0, 0.05)
wave9 = sounds.wave(piano(49), 100, 0.2)
wave10 = sounds.wave(piano(51), 100, 0.2)
wave11 = sounds.wave(piano(47), 100, 0.4)
wave115 = sounds.wave(100, 0, 0.05)
wave12 = sounds.wave(piano(47), 100, 0.4)
wave13 = sounds.wave(piano(45), 100, 0.2)
wave14 = sounds.wave(piano(44), 100, 0.2)
wave145 = sounds.wave(100, 0, 0.05)
wave15 = sounds.wave(piano(44), 100, 0.2)
wave16 = sounds.wave(piano(45), 100, 0.2)
wave17 = sounds.wave(piano(40), 100, 0.8)
tune = sounds.tune(wave1, wave2, wave3, wave4, wave45, wave5, wave6, wave7, wave75, wave8, wave85, wave9, wave10, wave11, wave115, wave12, wave13, wave14, wave145, wave15, wave16, wave17)
tune.write_to_wav()

#wave = obj.construct_wave()

# @dispatch(object, object)
# def generate_sine_wave(frequency, duration, amplitude = 4096, sample_rate = 44100):
#     t = np.linspace(0, duration, int(sample_rate * duration)) # discretized time interval
#     wave = amplitude * np.sin(2 * np.pi * frequency * t)      # generates our sine wave over the time interval constructed
#     return wave

# @dispatch(object, object, int)
# def generate_sine_wave(frequency, duration, amplitude, sample_rate = 44100):
#     t = np.linspace(0, duration, int(sample_rate * duration)) # discretized time interval
#     wave = amplitude * np.sin(2 * np.pi * frequency * t)      # generates our sine wave over the time interval constructed
#     return wave

# @dispatch(object, object, object)
# def generate_sine_wave(frequency, duration, amplitude, sample_rate = 44100):
#     print('stonks')

# def varying_amplitude(function, duration):
#     print('stonks')

# def write_to_wav(waves, file_name = "generic.wav", rate = 44100, wav_type = np.int16):
#     wavfile.write(file_name, rate, data = waves.astype(wav_type)) 

#wave = generate_sine_wave(440, 5, amplitude = 'five')
#write_to_wav(wave, "generic2.wav")
#wavfile.write("test.wav", rate = 44100, data = sine_wave.astype(np.int16))