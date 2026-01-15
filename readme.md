# 🍽️ Restaurant Outreach Agent (Frontend Lead Generator)

This project is a **local, AI-powered outreach agent** that helps a frontend developer find **real restaurant clients** and send them polite cold emails.

The agent:

* **Finds nearby restaurants** using free OpenStreetMap data (Overpass API)
* **Filters only restaurants without websites**
* **Generates professional AI-written cold emails** (with smart fallback)
* **Sends emails safely** with rate-limiting
* **Logs all activity locally** to avoid duplicates

The project is designed for **beginners** and runs **completely locally on your computer** with **no paid APIs required**.

---

## 🚀 What This Agent Does

When you run:

```bash
python agent.py
```

The agent will:

1. 🔍 **Search nearby restaurants** in your location (using free OpenStreetMap)
2. 🧹 **Filter restaurants without websites**
3. 📧 **Generate personalized AI emails** (or use fallback template)
4. ✉️ **Send emails safely** with rate-limiting
5. 📊 **Log results** in `data/contacts.csv`

This helps you get **frontend projects** without bidding platforms.

---

## 🧠 Tech Stack

* **Python 3.10+**
* **Overpass API (OpenStreetMap)** – FREE restaurant data, no API key needed ✅
* **OpenAI API** – AI email generation (with smart fallback template)
* **Gmail SMTP** – Email sending
* **Requests** – HTTP client for API calls
* **CSV logging** – Agent memory

---

## 📁 Project Structure

```
restaurant-agent/
│
├── agent.py                 # Main agent logic
├── config.py                # Configuration (API keys, location)
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
├── readme.md                # This file
├── data/
│   └── contacts.csv         # Contact history
└── utils/
    ├── search.py            # OpenStreetMap restaurant search
    ├── filter.py            # Filter restaurants without websites
    ├── ai_email.py          # AI email generation + fallback
    ├── email_sender.py      # Gmail SMTP sender
    ├── email_finder.py      # Email extraction (optional)
    └── logger.py            # CSV logging
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Python

Check if Python is installed:

```bash
python --version
```

If not, download from **[python.org](https://python.org)** and check **"Add to PATH"** during installation.

---

### 2️⃣ Clone or Download This Project

```bash
git clone https://github.com/vansharora21/restaurant-ai-.git
cd restaurant-ai-
```

Or download the ZIP file and extract it.

---

### 3️⃣ Create Virtual Environment (Recommended)

On **Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

On **Mac/Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `requests` – for Overpass API calls
- `python-dotenv` – for .env file support
- `openai` – for AI email generation
- `beautifulsoup4` – for HTML parsing (optional)

---

### 5️⃣ Create `.env` File

Create a `.env` file in the project root:

```env
OPENAI_API_KEY="sk-your-key-here"
LOCATION_COORDS="26.9124,75.7873"
EMAIL_ADDRESS="your@gmail.com"
EMAIL_PASSWORD="your_app_password"
```

**Get your credentials:**

1. **OPENAI_API_KEY** – Get from [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. **LOCATION_COORDS** – Use format: `"latitude,longitude"` (e.g., Jaipur: `"26.9124,75.7873"`)
3. **EMAIL_ADDRESS** – Your Gmail address
4. **EMAIL_PASSWORD** – Gmail App Password (NOT your regular password)
   - Enable 2FA on Gmail
   - Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
   - Generate a 16-character app password
   - Use that in `.env`

---

### 6️⃣ Create Data Directory

Make sure the `data/` folder exists:

```bash
mkdir data
```

Create `data/contacts.csv` with headers:

```csv
name,email,status,timestamp
```

---

## ▶️ Running the Agent

### Test Mode (Preview - No Emails Sent)

```bash
python agent.py
```

This will:
- ✅ Search for restaurants
- ✅ Filter them
- ✅ Generate emails
- ❌ NOT send emails (for safety)

Check the console output to review results.

---

## 🎯 Features

### ✅ Free Restaurant Data
- Uses **Overpass API** (OpenStreetMap data)
- **No API key required**
- Finds restaurants by coordinates + radius
- Extracts: name, location, website, phone, email, cuisine

### ✅ Smart Email Generation
- Uses **OpenAI API** for personalized emails
- **Automatic fallback** if OpenAI fails:
  - Uses professional template
  - Agent still works without API quota
  - Prevents agent from crashing

### ✅ Retry Logic
- Multiple Overpass endpoints for reliability
- Automatic retry on timeout/error
- Better error messages
- Handles rate limiting gracefully

### ✅ Safe Email Sending
- Rate-limited (4-5 seconds between emails)
- Logs all sent/failed emails
- Prevents duplicate messaging
- Respects anti-spam rules

### ✅ Local Logging
- All contacts saved to `data/contacts.csv`
- Tracks: name, email, status, timestamp
- Helps avoid sending duplicate emails

---

## 🔒 Anti-Spam & Ethics

**Important Guidelines:**

- ✅ Max 20-30 emails per day
- ✅ 4-5 second delay between emails
- ✅ Only message restaurants without websites
- ✅ Include opt-out language in emails
- ✅ Never message same restaurant twice
- ✅ Only for legitimate business outreach

This agent is designed for **ethical, value-based outreach**, not spam.

---

## 🐛 Troubleshooting

### "❌ Error querying Overpass API: 504 Server Error"

**Solution:** Overpass API servers are overloaded. The agent will automatically try alternative endpoints. Wait a few minutes and try again.

Check status: https://overpass-api.de/status

---

### "openai.RateLimitError: insufficient_quota"

**Solution:** Your OpenAI account has no API quota.

Options:
1. **Add billing** to [platform.openai.com/account/billing](https://platform.openai.com/account/billing)
2. **Use fallback emails** – Agent will still work with professional template
3. **Use local LLM** (Ollama) – No API key needed

---

### "❌ SMTPAuthenticationError: Login failed"

**Solution:** Gmail credentials are wrong.

Check:
- ✅ Using **App Password** (not regular Gmail password)
- ✅ 2FA is enabled on Gmail account
- ✅ No spaces in `.env` file
- ✅ Correct email format

---

### No restaurants found

Check:
- ✅ Correct coordinates in `LOCATION_COORDS`
- ✅ Format: `"latitude,longitude"` (e.g., `"26.9124,75.7873"`)
- ✅ Location has restaurants on OpenStreetMap
- ✅ Internet connection is working

---

## 📊 Output Example

```
🚀 Agent started...

🔍 Searching for restaurants using OpenStreetMap...
🔄 Trying Overpass endpoint: https://overpass-api.de/api/interpreter
✅ Successfully queried Overpass API
✅ Found 47 restaurants from OpenStreetMap

🧹 Filtering restaurants without websites...
5 restaurants have NO website

✉️ Preparing email for Pizza Palace
⚠️ OpenAI API error: insufficient_quota
💡 Using fallback email template instead...

✉️ Generating AI email for Pizza Palace...
✅ Email sent to pizza@example.com
📊 Logged in data/contacts.csv

🎯 Agent finished successfully.
```

---

## 🚀 Advanced Features

### Change Search Radius

In `agent.py`, modify:
```python
restaurants = get_restaurants(
    location=LOCATION_COORDS,
    radius=5000  # Change to 5km instead of 3km
)
```

---

### Use Different Location

In `.env`, change:
```env
LOCATION_COORDS="40.7128,-74.0060"  # New York
```

Common coordinates:
- **Jaipur**: 26.9124,75.7873
- **Delhi**: 28.7041,77.1025
- **Mumbai**: 19.0760,72.8777
- **NYC**: 40.7128,-74.0060
- **London**: 51.5074,-0.1278

---

### Use Local LLM (Ollama) Instead of OpenAI

Install [Ollama](https://ollama.ai), then run:
```bash
ollama pull mistral
ollama serve
```

Then update `utils/ai_email.py` to use local LLM. (I can help with this!)

---

## 📈 Future Improvements

- [ ] WhatsApp fallback messaging
- [ ] Facebook/Instagram email scraping
- [ ] Follow-up email automation
- [ ] Reply analysis using AI
- [ ] Web scraping for contact info
- [ ] CLI support (`--city jaipur --radius 5km`)
- [ ] Dashboard for email tracking

---

## 💡 Tips for Success

1. **Start small** – Test with 5-10 emails first
2. **Personalize emails** – The fallback template is generic but works
3. **Track responses** – Note which emails get replies
4. **Improve copy** – Adjust email template based on results
5. **Follow up** – Send 2-3 follow-ups to non-responders
6. **Build relationship** – Focus on value, not sales pitch

---

## 👤 Author

**Vansh Arora**  
Frontend Developer & AI Enthusiast

This project is built for learning, ethical outreach, and real-world freelancing.

---

## 📄 License

This project is open source and available under the MIT License.

---

✅ **Ready to find restaurant clients? Run `python agent.py` now!**
#   W E B D E V - J O B - F I N D E R  
 #   W E B D E V - J O B - F I N D E R  
 