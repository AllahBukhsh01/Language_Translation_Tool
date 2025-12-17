import streamlit as st
import pyperclip
from utils.translator import translate_text
from utils.tts import text_to_speech

st.set_page_config(page_title="AI Translator", layout="centered")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🌐 AI Language Translation Tool")

languages = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Arabic": "ar",
    "Hindi": "hi",
    "Chinese": "zh-cn"
}

# Session state for history
if "history" not in st.session_state:
    st.session_state.history = []

input_text = st.text_area("Enter text", height=120)

target_lang = st.selectbox("Target Language", languages.keys())

# 🔄 Real-time translation
if input_text.strip():
    translated_text, detected_lang = translate_text(
        input_text,
        languages[target_lang]
    )

    st.success(f"🧠 Detected Language: {detected_lang}")
    st.text_area("Translated Text", translated_text, height=120)

    # Save history
    st.session_state.history.append({
        "original": input_text,
        "translated": translated_text
    })

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📋 Copy"):
            pyperclip.copy(translated_text)
            st.toast("Copied to clipboard")

    with col2:
        audio = text_to_speech(translated_text, languages[target_lang])
        st.audio(audio)

# 📜 History
with st.expander("📜 Translation History"):
    for item in reversed(st.session_state.history[-5:]):
        st.markdown(f"**Original:** {item['original']}")
        st.markdown(f"**Translated:** {item['translated']}")
        st.markdown("---")
