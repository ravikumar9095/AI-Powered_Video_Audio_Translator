AI-Powered_Video_Audio_Translator
To convert a video one language into user desired language
Converts video audio from Hindi to Telugu using Python. This project integrates speech recognition, translation, and text-to-speech, and optionally supports AI-based voice conversion for natural output.

---

 Features

  Convert audio from one language to another in video files.
  Multi-speaker support: preserves different voices in the input.
  Optional AI/ML enhancement: deep learning-based voice conversion with gTTs.
  Supports real-time processing for short video clips.

---

## Tech Stack

    Python  
    MoviePy   – Video/audio editing
    Pydub   – Audio manipulation
    SpeechRecognition   – Speech-to-text
    Googletrans   – Translation
    gTTS   – Text-to-speech
    Optional AI  : PyTorch, Whisper, Coqui TTS

---

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/multi-video-language-converter.git
cd multi-video-language-converter

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

```python
from converter import VideoLanguageConverter

# Initialize converter
converter = VideoLanguageConverter(source_lang='hi', target_lang='te')

# Convert video
converter.convert('input_video.mp4', 'output_video.mp4')
```

  `source_lang`: Source language code (e.g., `'hi'` for Hindi)
  `target_lang`: Target language code (e.g., `'te'` for Telugu)

---

## Demo

You can add a GIF or screenshot here showing the input video and converted output.

---

## Optional AI/ML Enhancement

For   more natural voice conversion  :

```python
from ai_converter import AIVoiceConverter

ai_converter = AIVoiceConverter(source_lang='hi', target_lang='te')
ai_converter.convert('input_video.mp4', 'output_video_ai.mp4')
```

  Uses   Whisper   for speech recognition and   Coqui TTS   for voice synthesis.

---

## Contributing

Contributions are welcome! Please create a PR or raise an issue for improvements, bug fixes, or new features.

---

## License

MIT License © \CHITTIBOYINA RAVI KUMAR

---

If you want, I can   also make a super clean, one-page version with badges, GIF demo placeholders, and installation tips  —perfect for a professional GitHub project that impresses recruiters.

Do you want me to do that next?
