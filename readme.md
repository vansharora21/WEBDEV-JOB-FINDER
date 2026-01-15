# 🍽️ Restaurant Outreach Agent

### *AI‑Powered Frontend Lead Generator for Local Restaurants*

A **beginner‑friendly, fully local AI agent** that helps frontend developers discover **real restaurant clients** and send **ethical, professional cold emails** — without using paid map APIs or scraping shady data.

> 🎯 Built for learning, freelancing, and real‑world outreach — **not spam**.

---

## ✨ What This Project Does

When you run:

```bash
python agent.py
```

The agent automatically:

1. 🔍 **Finds nearby restaurants** using **free OpenStreetMap (Overpass API)**
2. 🧹 **Filters restaurants that do NOT have a website**
3. 📧 **Generates personalized outreach emails using AI**
4. ✉️ **Sends emails safely** with built‑in rate‑limiting
5. 📊 **Logs every action locally** to avoid duplicate outreach

This helps you **get frontend projects directly** — without freelancing platforms or bidding wars.

---

## 🧠 Tech Stack

| Tool                             | Purpose                                 |
| -------------------------------- | --------------------------------------- |
| **Python 3.10+**                 | Core language                           |
| **OpenStreetMap (Overpass API)** | Free restaurant data (no API key)       |
| **OpenAI API**                   | AI‑generated outreach emails (optional) |
| **Gmail SMTP**                   | Safe email sending                      |
| **Requests**                     | API communication                       |
| **CSV**                          | Local memory & logging                  |

> ✅ Runs **100% locally** on your computer

---

## 📁 Project Structure

```text
restaurant-agent/
│
├── agent.py              # Main agent runner
├── config.py             # Global configuration
├── requirements.txt      # Dependencies
├── .env                  # Environment variables
├── readme.md             # Documentation
│
├── data/
│   └── contacts.csv      # Outreach history
│
└── utils/
    ├── search.py         # OpenStreetMap queries
    ├── filter.py         # Website filtering logic
    ├── ai_email.py       # AI + fallback email generator
    ├── email_sender.py  # Gmail SMTP sender
    ├── email_finder.py  # Email extraction (optional)
    └── logger.py        # CSV logging utility
```

---

## ⚙️ Setup Guide

### 1️⃣ Install Python

Check if Python is installed:

```bash
python --version
```

If not, download from **[https://python.org](https://python.org)** and ensure **“Add to PATH”** is checked.

---

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/vansharora21/restaurant-ai-.git
cd restaurant-ai-
```

Or download the ZIP and extract it.

---

### 3️⃣ Create a Virtual Environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Installed packages:

* `requests`
* `python-dotenv`
* `openai`
* `beautifulsoup4` (optional)

---

### 5️⃣ Create `.env` File

Create a file named `.env` in the project root:

```env
OPENAI_API_KEY="sk-your-key-here"
LOCATION_COORDS="26.9124,75.7873"
EMAIL_ADDRESS="your@gmail.com"
EMAIL_PASSWORD="your_app_password"
```

#### 🔑 How to Get These Values

* **OpenAI API Key** → [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
* **Location Coords** → `latitude,longitude`
* **Gmail App Password** → [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

> ⚠️ Use a **Gmail App Password**, NOT your normal Gmail password

---

### 6️⃣ Create Data Directory

```bash
mkdir data
```

Create `data/contacts.csv`:

```csv
name,email,status,timestamp
```

---

## ▶️ Running the Agent

### 🧪 Test Mode (Highly Recommended)

```bash
python agent.py --test
```

✔ No real emails sent
✔ Uses mock restaurants
✔ Generates & previews emails
✔ Logs everything locally

Perfect for **testing, demos, and safety checks**.

---

### 📧 Live Outreach Mode

```bash
python agent.py
```

✔ Searches real restaurants
✔ Filters businesses without websites
✔ Sends real emails via Gmail
✔ 4–5 second delay between emails

> 🚨 Start with **5–10 emails/day**

---

## 🌟 Key Features

### ✅ Free Restaurant Data

* Powered by **OpenStreetMap**
* No API key required
* Auto‑retry with multiple endpoints

### ✅ Smart Email Generation

* AI‑generated personalized emails
* Automatic **fallback template** if AI fails
* Agent never crashes due to quota issues

### ✅ Safe Email Sending

* Built‑in rate limiting
* Duplicate prevention
* CSV‑based memory

### ✅ Ethical by Design

* Targets only businesses without websites
* Includes opt‑out language
* Local storage only — no data selling

---

## 🐛 Troubleshooting

### Gmail Authentication Error

✔ Enable **2‑Step Verification**
✔ Use **App Password**
✔ Paste password without spaces

If blocked → use test mode:

```bash
python agent.py --test
```

---

### Overpass API Timeout

✔ Servers may be overloaded
✔ Wait 20–30 minutes
✔ Test mode works instantly

Status: [https://overpass-api.de/status](https://overpass-api.de/status)

---

### OpenAI Quota Error

✔ Add billing **or**
✔ Let fallback email handle it automatically

---

## 📈 Customization

### Change Search Radius

```python
radius=5000  # 5km
```

### Change City

```env
LOCATION_COORDS="28.7041,77.1025"  # Delhi
```

---

## 🔮 Future Enhancements

* WhatsApp outreach
* Follow‑up automation
* Reply sentiment analysis
* Admin dashboard
* Local LLM support (Ollama)

---

## 👤 Author

**Vansh Arora**
Frontend Developer · AI Enthusiast

Built for learning, freelancing, and ethical outreach.

---

## 📄 License

MIT License — free to use, modify, and learn from.

---

🚀 **Ready to find real frontend clients?**
Run:

```bash
python agent.py
```
