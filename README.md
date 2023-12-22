# Lecture Tiktokifier 
Turn lectures into prime brainrot content.
### Why would I want this?
 A lot of students these days say that following lectures is too hard due to their shortened attention span. A lot of people would blame the fast paced content of TikTok as the primary culprit, but one striking example seemed to push against the 15-20 second attention span. That is the Reddit stories in which a text to speech voice narrates the story with subtitles for every single word. Typically a clip of some oddly satisfying, Minecraft parkour or Subway surfers content plays underneath. These videos have taken TikTok and Youtube Shorts by storm. [Example here](https://www.youtube.com/shorts/lDjLfbfDx5U). Who knows this might make you a better student!

### I'm sold, how does this work?
Using a modified version of OpenAI's Whisper, LinTO AI's open sourced [whisper-timestamped](https://github.com/linto-ai/whisper-timestamped) model can analyze any audio file and output a timestamp for every single word. This is perfect for our needs since our target audience has a very short attention span so flashing a word about every 0.2 seconds seems like a great idea for viewer retention.

This script will break down any input video file into an mp3 and run this audio through LinTO AI's model. Using the output from the model it will then generate a subtitle and time for each word and edit it into the bottom frame. The gameplay / attention grabbing video is then stitched to the bottom of the original lecture video for maximum viewer retention.

