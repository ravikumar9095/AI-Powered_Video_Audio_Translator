from moviepy.editor import VideoFileClip

def extract_video_audio():
    # Fixed path
    VIDEO_PATH = r"C:\Users\user\videotransulato\checking\testvideo.mp4"

    # Output file paths
    VIDEO_NO_AUDIO = r"C:\Users\user\videotransulato\checking\video_no_audio.mp4"
    AUDIO_PATH = r"C:\Users\user\videotransulato\checking\extracted_audio.wav"

    # Load video
    video = VideoFileClip(VIDEO_PATH)

    # Save video without audio
    video.without_audio().write_videofile(VIDEO_NO_AUDIO, codec="libx264")

    # Extract audio
    video.audio.write_audiofile(AUDIO_PATH)

    print("\n✅ Step 1 complete!")
    print(f"Silent video saved: {VIDEO_NO_AUDIO}")
    print(f"Extracted audio saved: {AUDIO_PATH}")
    return VIDEO_NO_AUDIO, AUDIO_PATH


if __name__ == "__main__":
    extract_video_audio()
