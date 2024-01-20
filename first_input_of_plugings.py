"""""
Converter using VST3 and Audio Unit plugins.

As mentioned in the bachelor thesis, I divide the data set into 3 parts,
one quarter of the data is slightly altered,
another quarter is heavily corrupted and the remaining half is moderately corrupted.
The number of audios is 29099 / 4 = 7275 (abgerundet),
with the if statment I can kwon what is the number of the audio, that is after the first quartel of the data.
Because not all audio number exists.
Just run the third_input_of_plugins.py, it will run the first and the sencond one automatically

"""""

# Load the necessary Libraries.
from pedalboard import Reverb, load_plugin, Pedalboard
from pedalboard.io import AudioFile

vst = load_plugin("C:\Program Files\Common Files\VST3\Correlometer.vst3")


counter1 = 0
item = 31834788
while item < 32940766:
    item += 1
    try:
        # Set the vst parameters.
        vst.ratio = 15
        vst.input_lvl_db = 2.4
        vst.makeup_db = 10
        vst.mix = 10
        vst.program = "2s, 48-band, steepest"
        vst.bypass = True

        # Read the audio file.
        with AudioFile("D:\\data\\common_voice_de_" + str(item)+ ".mp3", "r") as f:
            audio = f.read(f.frames)
            samplerate = f.samplerate
            board = Pedalboard([vst, Reverb()])

        # and run that pedalboard with the same VST instance!
            effected = board(audio, samplerate)

        with AudioFile("D:\\data1\\Con1_common_voice_de_" + str(item)+ ".mp3", 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)
	
        print("The audio data point number: " + str(item) + " is processed.")
        counter1 += 1
        if counter1 == 7275:
           item1 = item

    except ValueError as ve:
        print("This number does not exist: " + str(item))	

print("The number of processed Audio data in this step is: " + counter1)
        