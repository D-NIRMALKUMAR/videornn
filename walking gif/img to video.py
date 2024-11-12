from moviepy.editor import ImageClip

# Load the image
image_clip = ImageClip("w1/frame_1.png")

# Set the duration of the video to 60 seconds
image_clip = image_clip.set_duration(60)

# Set the frame rate (fps)
image_clip = image_clip.set_fps(24)

# Export the video as an MP4 file
image_clip.write_videofile("input_video.mp4", codec="libx264")
