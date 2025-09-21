import os
from pydub import AudioSegment

# Folder where sound files are stored
OUTPUT_DIR = r"C:/Users/user/videotransulato/outputs"

# Find all sound files and sort them numerically by their index
sound_files = [f for f in os.listdir(OUTPUT_DIR) if f.startswith("sound") and f.endswith(".wav")]

# Extract the number and sort properly
def sound_index(f):
    return int(''.join(filter(str.isdigit, f)))

sound_files.sort(key=sound_index)

print(f"🔹 Total sound files to merge: {len(sound_files)}")

# Merge audios
merged_audio = AudioSegment.silent(duration=0)  # start with empty audio
for f in sound_files:
    f_path = os.path.join(OUTPUT_DIR, f)
    audio = AudioSegment.from_wav(f_path)
    merged_audio += audio
    print(f"Added {f} to merged audio")

# Export final merged audio
final_path = os.path.join(OUTPUT_DIR, "merged_audio.wav")
merged_audio.export(final_path, format="wav")
print(f"\n✅ All sound files merged into: {final_path}")
