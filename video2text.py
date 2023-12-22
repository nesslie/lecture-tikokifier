import os
import whisper_timestamped


class ConvertToAudio:
    def __init__(self, filename: str):
        self.filename = filename
        self.output_file = ''

    def convert_2_wav(self, output_name: str):
        command1 = f"ffmpeg -i {self.filename} speech.mp3"
        command2 = f"ffmpeg -i speech.mp3 out/{output_name}"
        os.system(command1)
        os.system(command2)
        os.system("rm speech.mp3")
        self.output_file = f"out/{output_name}"
        return

    def convert_2_str(self):
        audio = whisper_timestamped.load_audio(self.output_file)
        model = whisper_timestamped.load_model("base")
        result = whisper_timestamped.transcribe(model, audio)
        return result
