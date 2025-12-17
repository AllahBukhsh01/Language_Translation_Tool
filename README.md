# 🌐 AI Language Translation Tool

An **industry-grade, AI-powered Language Translation Web Application** built using **Python and Streamlit**. The application provides **real-time translation**, **automatic language detection**, **dark mode UI**, **translation history**, **copy functionality**, and **text-to-speech support** using **Google Translate (googletrans)**.

This project is suitable for:
- Final Year Project (FYP)
- Portfolio showcase
- Internship / entry-level job applications
- Practical demonstration of NLP-based applications

---

## 🚀 Features

- 🧠 **Automatic Language Detection**  
  Detects the source language automatically without user input.

- 🔄 **Real-Time Translation**  
  Translation happens instantly as the user types text.

- 🌍 **Multi-Language Support**  
  Supports multiple international languages including English, Urdu, French, German, Spanish, Arabic, Hindi, and Chinese.

- 🎨 **Custom Dark Mode UI**  
  Modern and professional dark-themed interface using custom CSS.

- 📜 **Translation History**  
  Maintains recent translations during the session for quick reference.

- 📋 **Copy to Clipboard**  
  One-click copy button for translated text.

- 🔊 **Text-to-Speech**  
  Converts translated text into speech for better accessibility.

---

## 🛠️ Technology Stack

| Layer | Technology |
|------|-----------|
| Frontend | Streamlit |
| Backend | Python |
| Translation Engine | Google Translate (googletrans) |
| Text-to-Speech | gTTS |
| Styling | Custom CSS |
| IDE | Visual Studio Code |
| OS | Windows |

---

## 📁 Project Structure

```
Language_Translation_Tool/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
│
├── utils/
│   ├── translator.py      # Translation logic (Google Translate)
│   └── tts.py             # Text-to-Speech functionality
│
├── assets/
│   └── style.css          # Custom dark mode styling
│
└── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Language_Translation_Tool.git
cd Language_Translation_Tool
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

After running the command, the app will open automatically in your browser.

---

## 🧪 How It Works

1. User enters text into the input box.
2. Google Translate automatically detects the source language.
3. Text is translated into the selected target language in real time.
4. Translated text is displayed clearly.
5. User can:
   - Copy the translated text
   - Listen to the translated audio
   - View recent translation history

---

## 📌 Supported Languages

- English
- Urdu
- French
- German
- Spanish
- Arabic
- Hindi
- Chinese

(More languages can be added easily.)

---

## 🎯 Use Cases

- Language learning
- Travel assistance
- International communication
- Educational demonstrations
- NLP-based academic projects

---

## 🧩 Future Enhancements

- User authentication
- Persistent database for translation history
- WhatsApp-style chat UI
- Mobile responsive layout
- Cloud deployment (Streamlit Cloud / Docker)

---

## 🧑‍💻 Author

**Allah Bukhsh**
**Portfolio:** https://allahbukhsh.lovable.app/
**LinkedIn:** www.linkedin.com/in/allah-bukhsh-baloch   

---

## 📜 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this project for educational and personal use.

---

## ⭐ Acknowledgements

- Streamlit Community
- Google Translate
- Open-source Python ecosystem

---

If you find this project helpful, feel free to ⭐ star the repository and share it!

