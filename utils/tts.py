from gtts import gTTS
import tempfile

def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang)
    file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(file.name)
    return file.name
