#IMPORTS
import numpy as np
from scipy.io import wavfile
from multipledispatch import dispatch

@dispatch(object, object)
def generate_sine_wave(frequency, duration, amplitude = 4096, sample_rate = 44100):
    t = np.linspace(0, duration, int(sample_rate * duration)) # discretized time interval
    wave = amplitude * np.sin(2 * np.pi * frequency * t)      # generates our sine wave over the time interval constructed
    return wave

@dispatch(object, object, int)
def generate_sine_wave(frequency, duration, amplitude, sample_rate = 44100):
    t = np.linspace(0, duration, int(sample_rate * duration)) # discretized time interval
    wave = amplitude * np.sin(2 * np.pi * frequency * t)      # generates our sine wave over the time interval constructed
    return wave

@dispatch(object, object, object)
def generate_sine_wave(frequency, duration, amplitude, sample_rate = 44100):
    print('stonks')

def varying_amplitude(function, duration):
    print('stonks')

def write_to_wav(waves, file_name = "generic.wav", rate = 44100, wav_type = np.int16):
    wavfile.write(file_name, rate, data = waves.astype(wav_type)) 

wave = generate_sine_wave(440, 5, amplitude = 'five')
write_to_wav(wave)
#wavfile.write("test.wav", rate = 44100, data = sine_wave.astype(np.int16))