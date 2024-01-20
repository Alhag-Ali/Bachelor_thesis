"""""
Converter using VST3 and Audio Unit plugins.

As mentioned in the bachelor thesis, I divide the data set into 3 parts,
one quarter of the data is slightly altered,
another quarter is heavily corrupted and the remaining half is moderately corrupted.

"""""

from pedalboard import Pedalboard, Chorus, Delay, Gain
from pedalboard import Reverb, NoiseGate, PitchShift
from pedalboard.io import AudioFile
from first_input_of_plugings import item1

counter2 = 0

while item1 < 32940766:
    item1 += 1
    try:
        # Read in a whole audio file:
        with AudioFile("D:\\data1\\Con1_common_voice_de_" + str(item1) + ".mp3", "r") as f:
            audio = f.read(f.frames)
            samplerate = f.samplerate

        # Make a Pedalboard object, containing multiple plugins:
        board = Pedalboard([Chorus(),
                            Reverb(room_size=0.5),
                            Delay(delay_seconds=0.10, mix=1.0),
                            Gain(gain_db=-3),
                            NoiseGate(threshold_db=-100.0),
                            PitchShift(semitones=2),
                            ])

        # Run the audio through this pedalboard!
        effected = board(audio, samplerate)

        # Write the audio back as new file:
        with AudioFile("D:\\data2\\Con2_common_voice_de_" + str(item1) + ".mp3", 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)

        print("The audio data point number: " + str(item1) + " is processed.")
        counter2 += 1
        if counter2 == 14550:
            item2 = item1

    except ValueError as ve:
        print("This number does not exist: " + str(item1))		
        
print("The number of processed Audio data in this step is: " + counter2)       
        