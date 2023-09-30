from moviepy.editor import *
import os
IMAGEMAGICK_BINARY = "C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\convert.exe"
os.environ["IMAGEIO_FFMPEG_EXE"] = "C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\convert.exe"

from moviepy.editor import *

background_image = ImageClip("Liam.jpeg")


text = "Il était une fois, dans un petit village au cœur d'une vallée verdoyante, un jeune garçon nommé Liam. Liam était un rêveur, toujours plongé dans les pages de ses livres préférés."
words = text.split()  


video_clips = []
current_time = 0  

for word in words:
    word_clip = TextClip(word, fontsize=30, color="white")
    word_duration = len(word) * 0.1  
    word_clip = word_clip.set_duration(word_duration)
    word_clip = word_clip.set_position("center")
    word_clip = word_clip.set_start(current_time)
    video_clips.append(word_clip)
    current_time += word_duration


final_video = CompositeVideoClip([background_image.set_duration(current_time)] + video_clips)


final_video.write_videofile("output_video.mp4", fps=24)
