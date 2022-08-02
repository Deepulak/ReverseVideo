from moviepy.editor import *
import moviepy.video.fx.all as vfx

clip = VideoFileClip("sample.mp4").subclip(0, 9)

sub = clip.ipython_display(width=720)

sub = sub.fx(vfx.crop, x1=115, x2=399, y1=0, y2=288)

clip2 = sub.speedx(final_duration=6)

clip3 = clip2.fx(vfx.time_mirror)

final = concatenate_videoclips([clip2, clip3])

final.to_gif("boomerang_like_gif.gif", fps=25)