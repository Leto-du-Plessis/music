#IMPORTS
import numpy as np
#from scipy.io import wavfile
#from multipledispatch import dispatch
import sounds

def linear_filter(length, target):
    x = np.linspace(0, 1, int(length * (target[1] - target[0])))
    x = np.flip(x)
    return x

# note = sounds.piano_note("A4")
# wave1 = sounds.wave(note.get_frequency(), 100, 10)

# tune = sounds.tune(wave1)
# tune.apply_volume_filter(linear_filter, [0.25, 1])
# tune.produce_waveform()
# tune.write_to_wav()

sequence = sounds.piano_sequence("B4 G#4 E4 G#4 B4 G#4 B4 E4 B4 G#4 B4 E4")
tune = sequence.compile_wave(100, 152, "minim")
tune.write_to_wav()