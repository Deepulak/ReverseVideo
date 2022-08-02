from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("sample.mp4")

videoClip.write_gif("sample.gif")