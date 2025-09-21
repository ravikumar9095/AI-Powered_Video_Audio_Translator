import os
from pydub import AudioSegment, silence
import speech_recognition as sr

# Ask user for audio language
print("🌍 Enter the audio language code (examples: en-IN for English, te-IN for Telugu, hi-IN for Hindi):")
LANG_CODE = input("Language code: ").strip()

# Paths
OUTPUT_DIR = r"C:/Users/user/videotransulato/outputs"
AUDIO_PATH = r"C:/Users/user/videotransulato/checking/extracted_audio.wav"
os.makedirs(OUTPUT_DIR, exist_ok=True)

sound = AudioSegment.from_wav(AUDIO_PATH)
recognizer = sr.Recognizer()

# Split audio into sentences by detecting silence
chunks = silence.split_on_silence(
    sound,
    min_silence_len=500,
    silence_thresh=sound.dBFS - 14,
    keep_silence=300
)

print(f"🔎 Detected {len(chunks)} sentence-like chunks")

# To track time positions
current_time = 0
timings_file = os.path.join(OUTPUT_DIR, "timings.txt")

with open(timings_file, "w", encoding="utf-8") as tf:
    for idx, chunk in enumerate(chunks, start=1):
        start_time = current_time
        end_time = current_time + len(chunk)
        current_time = end_time  # update for next chunk

        # Save temporary chunk
        chunk_path = os.path.join(OUTPUT_DIR, f"temp_chunk{idx}.wav")
        chunk.export(chunk_path, format="wav")

        with sr.AudioFile(chunk_path) as source:
            audio_data = recognizer.record(source)
            try:
                # Recognize text in user-selected language
                text = recognizer.recognize_google(audio_data, language=LANG_CODE)

                # Save text to file
                filename = os.path.join(OUTPUT_DIR, f"file{idx}.txt")
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(text.strip() + "\n")

                # Save timing + filename for future combining
                tf.write(f"{start_time/1000:.2f}-{end_time/1000:.2f}s → {filename}\n")

                print(f"✅ Saved sentence: {filename} ({start_time/1000:.2f}-{end_time/1000:.2f}s)")

            except sr.UnknownValueError:
                # Save unrecognized audio
                filename = os.path.join(OUTPUT_DIR, f"sound{idx}.wav")
                chunk.export(filename, format="wav")

                # Save timing info
                tf.write(f"{start_time/1000:.2f}-{end_time/1000:.2f}s → {filename}\n")

                print(f"⚠️ Unrecognized → saved audio: {filename} ({start_time/1000:.2f}-{end_time/1000:.2f}s)")

print(f"\n📝 All timings saved in: {timings_file}")
