# IMPORTS
import numpy as np
from scipy.io import wavfile

class wave:
    """
    A wave object serves to construct a sine wave with a particular frequency, volume and duration. This object can be edited using the methods 'write_frequency(frequency)', 'write_volume(volume)' and 'write_duration(duration)'. The method 'construct wave' returns a
    numpy array containing the discretized sine wave described by the wave object. This object is the basic building block of sounds.
    """

    def __init__(self, frequency, volume, duration, samplerate = 44100):
        self.frequency = frequency
        self.amplitude = volume / 100 * 4096 # here we consider an amplitude of 4096 to be 100% volume
        self.duration = duration
        self.samplerate = samplerate      # generally best to leave as defualt
        self.filter = None                # placeholder, I suspect I will remove this field.
    
    def construct_wave(self):
        """
        The construct_wave method returns a numpy array of values describing the discretized sine wave.
        """
        t = np.linspace(0, self.duration, int(self.samplerate * self.duration)) # discretized time interval
        wave = self.amplitude * np.sin(2 * np.pi * self.frequency * t)          # generates our sine wave over the time interval constructed
        return np.array(wave)
    
    def write_frequency(self, frequency):
        """
        The write_frequency method updates the frequency of the wave object.
        """
        self.frequency = frequency
    
    def write_volume(self, volume):
        """
        The write_volume method updates the volume (amplitude) of the wave object.
        """
        self.volume = volume
    
    def write_duration(self, duration):
        """
        The write_duration method updates the duration of the wave object.
        """
        self.duration = duration
    
    def get_stats(self):
        print('Specifications for wave object:')
        print('Frequency: ' + self.frequency)
        print('Volume: ' + self.volume)
        print('Duration: ' + self.duration)

class tune:

    def __init__(self, *args, construction_type = 'append'):

        values = np.array([])
        for arg in args:
            if type(arg) == wave and construction_type == 'append':
                values = np.append(values, arg.construct_wave())
            elif type(arg) == wave and construction_type == 'overlay':
                arg = arg.construct_wave()
                length = max(len(arg), len(values))
                if len(values) != length:
                    values = np.append(values, np.zeros(length - len(values)))
                if len(arg) != length:
                    arg = np.append(arg, np.zeros(length - len(arg)))
                values = values + arg
        self.values = values

    def write_to_wav(self, file_name = "output.wav", rate = 44100, wav_type = np.int16):
        wavfile.write(file_name, rate, data = self.values.astype(wav_type)) 
