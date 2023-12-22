from moviepy.editor import *
from moviepy.video.fx.all import crop


class VideoCreator:
    def __init__(self, subtitleData, audioFile, videoFile):
        self.subtitleData = subtitleData
        self.subtitleClip = []
        self.audioChunks = []
        self.audioClip: AudioClip = AudioFileClip(f"out/{audioFile}")
        self.lectureVideo: VideoClip = VideoFileClip(videoFile).set_duration(
            self.audioClip.duration
        )
        self.videoClip: VideoClip = VideoFileClip("videos/1.mp4").resize((1080, 990))
        self.videoClip = self.videoClip.set_duration(self.audioClip.duration)
        self.lectureVideo = self.lectureVideo.resize((1080, 990))
        self.finalVideo = clips_array([[self.lectureVideo], [self.videoClip]])

    def createBackground(self):
        return

    def createSubtitles(self):
        print("Creating subtitles...")
        for segment in self.subtitleData["segments"]:
            for word in segment["words"]:
                start = word["start"]
                end = word["end"]
                text = word["text"].upper()
                subtitle = TextClip(
                    text,
                    size=(990, 400),
                    fontsize=180,
                    color="white",
                    font="Impact",
                    method="caption",
                    stroke_width=7,
                    stroke_color='black'
                ).set_start(start)
                subtitle = subtitle.set_start(start, change_end=True).set_duration(
                    end - start
                )
                self.subtitleClip.append(subtitle)
        print("Subtitles created!")

    def createVideo(self):
        self.createSubtitles()
        subtitles = CompositeVideoClip(self.subtitleClip)
        subtitles = CompositeVideoClip(
            [self.videoClip, subtitles.set_position(("center", "center"))]
        )
        final_clip = clips_array([[self.lectureVideo], [subtitles]])
        final_clip = final_clip.set_audio(self.audioClip)
        final_clip.write_videofile(
            "out/output.mp4",
            fps=24,
            codec="libx264",
            audio_codec="aac",
            temp_audiofile="temp-audio.m4a",
            remove_temp=True,
        )
        final_clip.close()
        self.videoClip.close()
        self.audioClip.close()
