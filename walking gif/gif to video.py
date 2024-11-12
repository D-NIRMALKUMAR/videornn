from moviepy.editor import *

# Load the GIF file
gif_clip = VideoFileClip("w2.gif")

# Calculate the number of times to loop the GIF to reach 1 minute (60 seconds)
loop_count = int(60 / gif_clip.duration)

# Repeat the GIF clip
video_clip = concatenate_videoclips([gif_clip] * loop_count)

# Set the final duration to 1 minute (in case it slightly exceeds due to rounding)
video_clip = video_clip.subclip(0, 60)

# Export the video as MP4
video_clip.write_videofile("output_video.mp4", codec="libx264", fps=24)
