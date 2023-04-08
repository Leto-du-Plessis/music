# IMPORTS
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

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
    """
    A tune object is a simple mathematical function describing a specified sound wave. The object wrapper exists to provide methods to operate on tune objects in some unified way.
    """

    def __init__(self, *args, construction_type = 'append'):
        
        values = np.array([])
        for arg in args: #each arg should be provided as a wave object to be converted into a single tune object.
            if type(arg) == wave and construction_type == 'append':    #simply concatenates all provided wave objects
                values = np.append(values, arg.construct_wave())
            elif type(arg) == wave and construction_type == 'overlay': #overlays wave objects when converting to a tune object to create a compound sound wave
                arg = arg.construct_wave()
                length = max(len(arg), len(values))
                if len(values) != length:                              #these two if statements deal with combining wave objects of different lengths if the overlay method is selected
                    values = np.append(values, np.zeros(length - len(values)))
                if len(arg) != length:
                    arg = np.append(arg, np.zeros(length - len(arg)))
                values = values + arg
            else:
                print("Please provide wave objects to be converted into a tune object.") #ghetto error message nyeeeeh don't like
        self.values = values 

    def apply_volume_filter(self, filter, target = [0,1]):

        target = (len(self.values) * np.array(target)).astype(int)
        filter_discrete = filter(target[1] - target[0], [0,1])
        chunk1 = np.append(self.values[0 : target[0]], np.multiply(self.values[target[0] : target[1]], filter_discrete))
        self.values = np.append(chunk1, self.values[target[1] : len(self.values)])

    def produce_waveform(self):
        t = np.linspace(0, len(self.values), len(self.values))
        plt.plot(t, self.values)
        plt.ylabel("Amplitude")
        plt.xlabel("t * frequency") # I don't think this is actually accurate (true) ... sample rate?? 
        plt.show()

    def write_to_wav(self, file_name = "output.wav", rate = 44100, wav_type = np.int16):
        wavfile.write(file_name, rate, data = self.values.astype(wav_type)) 

class piano_note:

    def __init__(self, string):
        string_list = list(string)
        if len(string_list) == 1:
            self.symbol = string_list[0]
            self.semitone = None
            self.octave = 4
        elif len(string_list) == 2:
            self.symbol = string_list[0]
            self.semitone = None
            self.octave = string_list[1]
        elif len(string_list) == 3:
            self.symbol = string_list[0]
            self.semitone = string_list[1]
            self.octave = string_list[2]

    def get_frequency(self):
        if self.semitone == None:
            symbol_lookup = dict([('A', 1), ('B', 3), ('C', 4), ('D', 6), ('E', 8), ('F', 9), ('G', 11)])
            if self.symbol == 'A' or self.symbol == 'B':
                num = symbol_lookup[self.symbol] + 12 * int(self.octave)
            else:
                num = symbol_lookup[self.symbol] + 12 * (int(self.octave) - 1) # this is kinda fucky ... me no likey 
        else:
            symbol_lookup = dict([("A#", 2), ("B$", 2), ("C#", 5), ("D$", 5), ("D#", 7), ("E$", 7), ("F#", 10), ("G$", 10), ("G#", 12), ("A$", 12)])
            if self.symbol == 'A' or self.symbol == 'B':
                num = symbol_lookup[self.symbol + self.semitone] + 12* int(self.octave)
            else:
                num = symbol_lookup[self.symbol + self.semitone] + 12 * (int(self.octave) - 1)
        return 2 ** ((num - 49)/12) * 440
    
class piano_sequence:

    def __init__(self, string):
        string_list = string.split(' ')
        piano_notes = []
        for element in string_list:
            piano_notes.append(piano_note(element))
        self.note_sequence = piano_notes

    def compile_wave(self, volume, tempo, note_value = "crotchet"): 
        note_value_lookup = dict([("breve", 2), ("semibreve", 1), ("minim", 0.5), ("crotchet", 0.25), ("quaver", 0.125), ("semiquaver", 1/16), ("demisemiquaver", 1/32)])
        if type(note_value) == str: #checks for a single note_value specified, versus a string of provided note values
            waves = ()
            for note in self.note_sequence:
                waves += (wave(note.get_frequency(), volume, (60/tempo) * note_value_lookup[note_value]), )
        else:
            waves = ()
            for i in range(len(self.note_sequence)):
                waves += (wave(self.note_sequence[i].get_frequency(), volume, (60/tempo) * note_value_lookup[note_value[i]]), )
        return tune(*waves)