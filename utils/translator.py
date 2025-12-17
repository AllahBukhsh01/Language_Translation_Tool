from googletrans import Translator

translator = Translator()

def translate_text(text, target_lang):
    result = translator.translate(text, dest=target_lang)
    return result.text, result.src
