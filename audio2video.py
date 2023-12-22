from moviepy.editor import *
from moviepy.video.fx.all import crop
import random
import math


class VideoCreator:
    def __init__(self, subtitleData, audioFile):
        self.subtitleData = subtitleData
        self.subtitleClip = []
        self.audioChunks = []
        self.audioClip: AudioClip = AudioFileClip(f'out/{audioFile}')
        self.videoClip: VideoClip = VideoFileClip("videos/1.mp4")
        (w, h) = self.videoClip.size
        crop_width = h * 9/16
        # x1,y1 is the top left corner, and x2, y2 is the lower right corner of the cropped area.

        x1, x2 = (w - crop_width)//2, (w+crop_width)//2
        y1, y2 = 0, h
        self.videoClip = crop(self.videoClip, x1=x1, y1=y1, x2=x2, y2=y2)
        self.videoClip = self.videoClip.set_duration(self.audioClip.duration)
        self.videoStartPoint = random.randint(0, math.floor(self.videoClip.duration) - math.floor(self.audioClip.duration))

    def createSubtitles(self):
        print("Creating subtitles...")
        for segment in self.subtitleData['segments']:
            for word in segment['words']:
                audio_chunk = self.audioClip.subclip(word['start'], word['end'])
                self.audioChunks.append(audio_chunk)
                start = word['start'] 
                end = word['end'] 
                text = word['text'].upper()
                subtitle = TextClip(text, fontsize=40, color='white', font='Helvetica-Bold').set_start(start)
                subtitle = subtitle.set_duration(end - start)
                subtitle = subtitle.set_end(end)    
                self.subtitleClip.append(subtitle)
        print("Subtitles created!")
                
    def createVideo(self):
        self.createSubtitles()
        subtitles = concatenate_videoclips(self.subtitleClip)
        audio = concatenate_audioclips(self.audioChunks)
        final_clip = CompositeVideoClip([self.videoClip, subtitles.set_pos(('center', 'center'))])
        final_clip = final_clip.set_audio(audio)
        final_clip.write_videofile("output.mp4", fps=24, codec="libx264")
        final_clip.close()
        self.videoClip.close()
        self.audioClip.close()



