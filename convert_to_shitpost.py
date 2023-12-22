import sys
import video2text
import audio2video

# get filename arguments and convert mp4 to wav
video_filename = ""
audio_filename = "cock.mp3"
if len(sys.argv) > 1:
    video_filename = sys.argv[1]
    converter = video2text.ConvertToAudio(video_filename)
    converter.convert_2_wav(audio_filename)

# start transcribing the filename
text_data = converter.convert_2_str()
creator = audio2video.VideoCreator(text_data, audio_filename, video_filename)
creator.createVideo()
converter.clear_files()
