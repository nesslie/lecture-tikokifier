import sys
import video2text
import audio2video

# get filename arguments and convert mp4 to wav
filename = ''
audio_filename = "cock.wav"
if len(sys.argv) > 1:
    filename = sys.argv[1]
    converter = video2text.ConvertToAudio(filename)
    converter.convert_2_wav(audio_filename)

# start transcribing the filename
text_data = converter.convert_2_str()
creator = audio2video.VideoCreator(text_data, audio_filename)
creator.createVideo()

# testing

