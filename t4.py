from moviepy.editor import VideoFileClip, AudioFileClip
import os

# Paths
VIDEO_PATH = r"C:/Users/user/videotransulato/checking/video_no_audio.mp4"  # original video
MERGED_AUDIO_PATH = r"C:/Users/user/videotransulato/outputs/merged_audio.wav"
OUTPUT_VIDEO_PATH = r"C:/Users/user/videotransulato/outputs/final_video.mp4"

# Load video and audio
video = VideoFileClip(VIDEO_PATH)
audio = AudioFileClip(MERGED_AUDIO_PATH)

# Set new audio to the video
final_video = video.set_audio(audio)

# Export final video
final_video.write_videofile(OUTPUT_VIDEO_PATH, codec="libx264", audio_codec="aac")

print(f"✅ Video with merged audio saved: {OUTPUT_VIDEO_PATH}")
