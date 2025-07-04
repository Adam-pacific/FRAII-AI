

# 🤖 FRAII AI — Multilingual Voice AI Assistant with Self-Healing Automation(Prototype) 

🚀 Live Demo: [Click Here to Try FRAII AI](https://adam-pacific-fraii-ai-fraii-ai-kp5tjr.streamlit.app/)  
📁 GitHub: [github.com/Adam-pacific/FRAII-AI](https://github.com/Adam-pacific/FRAII-AI)

--

## 💡 Overview

**FRAII AI** (pronounced *Free AI*) is a multilingual, voice-powered AI assistant built using **Streamlit**, capable of:

- Transcribing voice queries in **English, Tamil**, and **Hindi**
- Handling **CSV/XLSX file uploads**, detecting & fixing missing values
- Auto-generating **data summaries**
- Supporting **natural language chat + audio replies**
- Sending **automated emails**
- Fetching the **latest AI news**
- Running **browser automation**
- Storing and displaying **session memory**

This project is a prototype for next-gen **HyperAutomation** tools tailored to business operations in regional languages.

---

## 🧠 Core Features

| Feature | Description |
|--------|-------------|
| 🎙️ Voice Input | Supports English (Profit), Tamil (Laabam / லாபம்), and Hindi (Munafa / मुनाफा) |
| 📊 CSV/XLSX Upload & Fix | Detects and fixes missing values in uploaded datasets |
| 🧾 Summary Generator | Shows row/column stats, missing data reports, and basic analytics |
| 💬 Chat-based QA | Text and voice chat interface with multilingual responses |
| 📧 Email Automation | Sends reports and insights via Gmail SMTP (App Password-based) |
| 📰 News Fetcher | Scrapes and displays latest AI/ML tech news |
| 🤖 Browser Automation | Auto-fills online forms using Selenium (demo version) |
| 💾 Memory Viewer | Stores and displays uploaded files, fixes, and user queries |

---

## 🧱 Tech Stack

| Category         | Tools/Libs Used                             |
|------------------|---------------------------------------------|
| **Frontend UI**   | Streamlit                                   |
| **Voice & TTS**   | SpeechRecognition, gTTS                     |
| **Multilingual NLP** | langdetect, custom token-based rules     |
| **Data Analysis** | Pandas                                      |
| **Automation**    | Selenium                                    |
| **Email Service** | SMTP (Gmail App Password)                   |
| **News Fetching** | BeautifulSoup, Requests                     |
| **Deployment**    | Streamlit Cloud                             |
| **AI Integration**| OpenAI GPT (planned for summarizer module)  |

---

## 🌍 Supported Languages

- 🇬🇧 **English** (Profit)
- 🇮🇳 **Tamil** (லாபம் / Laabam)
- 🇮🇳 **Hindi** (मुनाफा / Munafa)

All supported languages work for both voice transcription and localized audio/text responses.

---

## 🧪 What’s Working Now

✅ Functional modules:
- File Upload + Fix
- Summary Generator
- Text & Voice Chat
- Email Automation
- AI/ML News Feed
- Browser Automation
- Session Memory Panel

---

## 🔜 Planned Enhancements

- 🤖 Add GPT-powered smart data summaries
- 📈 Add graphical charts using Plotly / Matplotlib
- 📬 Switch to Gmail API / SendGrid for email stability
- 🌐 Add more Indian languages (e.g., Telugu, Kannada, Bengali)
- 🧠 Build domain-specific decision agents (HR, Finance, Legal)

---

## 🛠️ How to Run Locally

```bash
git clone https://github.com/Adam-pacific/FRAII-AI.git
cd FRAII-AI
pip install -r requirements.txt
streamlit run app.py

✅ Ensure you have:

ChromeDriver (for Selenium)

Gmail App Password set up for email features

.env for sensitive keys (if using OpenAI or SMTP credentials)



---

🙋‍♂️ Author

F. A. Adam Ahamed
💼 AI Engineer, Innovator, and Automation Enthusiast
🌐 LinkedIn  :https://www.linkedin.com/in/adam-ahamed/| 📨 Email adamahamed953@gmail.com


---

🏁 Final Notes

This project is actively maintained and evolving toward a full-fledged multilingual AI automation platform for Indian businesses.
Your feedback, stars ⭐, and forks 🍴 are appreciated!




