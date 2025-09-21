import os
from googletrans import Translator
from gtts import gTTS
from pydub import AudioSegment

# ---------------- Paths ----------------
OUTPUT_DIR = r"C:/Users/user/videotransulato/outputs"
TIMINGS_FILE = os.path.join(OUTPUT_DIR, "timings.txt")

# Create output folder if not exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------- User Input ----------------
print("🌍 Enter destination language code (examples: en for English, te for Telugu, hi for Hindi):")
DEST_LANG = input("Destination language code: ").strip()

translator = Translator()

# ---------------- Helper Function ----------------
def adjust_duration(audio, target_ms):
    """Match audio length to target duration by padding or speeding up."""
    if not target_ms:
        return audio  # no adjustment if duration unknown

    current_ms = len(audio)
    if current_ms < target_ms:
        # pad silence at end
        silence = AudioSegment.silent(duration=target_ms - current_ms)
        return audio + silence
    elif current_ms > target_ms:
        # speed up proportionally
        speed_factor = current_ms / target_ms
        return audio._spawn(audio.raw_data, overrides={
            "frame_rate": int(audio.frame_rate * speed_factor)
        }).set_frame_rate(audio.frame_rate)
    else:
        return audio

# ---------------- Process timings.txt ----------------
with open(TIMINGS_FILE, "r", encoding="utf-8") as tf:
    lines = tf.readlines()

for line in lines:
    line = line.strip()
    if not line or "→" not in line:
        continue

    timing_part, file_path = line.split("→")
    file_path = file_path.strip()
    base_name = os.path.basename(file_path)

    # Extract duration
    duration_ms = None
    try:
        timing_part = timing_part.replace("s", "").replace("–", "-").strip()
        start_str, end_str = timing_part.split("-")
        duration_ms = int((float(end_str.strip()) - float(start_str.strip())) * 1000)
    except:
        pass

    # If text file (recognized sentence)
    if base_name.startswith("file") and base_name.endswith(".txt"):
        file_number = ''.join(filter(str.isdigit, base_name))  # extract number from fileX.txt
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().strip()

        # Translate text
        translated = translator.translate(text, dest=DEST_LANG).text

        # Convert to speech (gTTS)
        temp_path = os.path.join(OUTPUT_DIR, "temp_tts.mp3")
        tts = gTTS(translated, lang=DEST_LANG)
        tts.save(temp_path)

        # Load with pydub
        audio = AudioSegment.from_file(temp_path, format="mp3")

        # Adjust duration
        audio = adjust_duration(audio, duration_ms)

        # Save as WAV with same file number
        sound_name = f"sound{file_number}.wav"
        sound_path = os.path.join(OUTPUT_DIR, sound_name)
        audio.export(sound_path, format="wav")

        print(f"✅ Converted {base_name} → {sound_name} (duration matched {duration_ms/1000:.2f}s)" if duration_ms else f"✅ Converted {base_name} → {sound_name} (duration unknown)")

    # Skip already audio files
    elif base_name.startswith("sound") and base_name.endswith(".wav"):
        print(f"⚠️ Skipped {base_name} (already audio)")
