"""""
Converter using VST3 and Audio Unit plugins.

As mentioned in the bachelor thesis, I divide the data set into 3 parts,
one quarter of the data is slightly altered,
another quarter is heavily corrupted and the remaining half is moderately corrupted.

"""""

from pedalboard import Pedalboard, Chorus, Distortion, Gain, Reverb
from pedalboard import Bitcrush, NoiseGate, Chain
from pedalboard.io import AudioFile
from second_input_of_plugins import item2

counter3 = 0
while item2 < 32940766:
    item2 += 1 
    try:
        # Read in a whole audio file:
        with AudioFile("D:\\data2\\Con2_common_voice_de_" + str(item2) + ".mp3", "r") as f:
            audio = f.read(f.frames)
            samplerate = f.samplerate

        # Make a Pedalboard object, containing multiple plugins:
        board = Pedalboard([Chorus(),
                            Reverb(room_size=0.60),
                            Distortion(drive_db=20),
                            Bitcrush(bit_depth=15),
                            Chain(),
                            Gain(gain_db=-3),
                            NoiseGate(threshold_db=-150.0,
                            ratio=10,attack_ms=1.0,
                            release_ms=100.0)
                            ])

        # Run the audio through this pedalboard!
        effected = board(audio, samplerate)

        # Write the audio back as new file:
        with AudioFile("D:\\data3\\Con3_common_voice_de_32155565.mp3", 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)
	
        counter3 += 1
        print("The audio data point number: " + str(item2) + " is processed.")

    except ValueError as ve:
        print("This number does not exist: " + str(item2))		

print("The number of processed Audio data in this step is: " + counter3)   
