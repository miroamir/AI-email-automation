# AI Recruitment Email Automation 💼📧

This is a custom AI-powered recruitment outreach tool — built as one of many automation services under the **MiroMate** platform.

It uses GPT-4 to write highly personalized emails and sends them via Gmail SMTP — removing all manual effort for recruiters and helping them get faster replies, better candidates, and more placements.

> 👨‍💻 Built by AutoMiro — AI-powered automations for modern businesses.

---

## 🚀 What It Does

- ✅ Writes recruitment emails using GPT-4o  
- ✅ Sends messages automatically through Gmail  
- ✅ Uses your real tone, company info, and candidate data  
- ✅ Saves hours of repetitive work  
- ✅ Designed for real outreach, not spam

---

## 🧠 Powered By

- Python 3.10  
- FastAPI  
- OpenAI (GPT-4o)  
- Gmail SMTP (App Passwords)  
- Pydantic, `smtplib`, `python-dotenv`

---

## 📦 Example Use Case

Recruiter inputs:

- Candidate: *Alex Johnson*  
- Role: *Frontend Developer*  
- Company: *TechCorp*  
- Recruiter: *Samantha*

The tool instantly generates and sends a personalized message like:

> “Hi Alex, I’m Samantha from TechCorp. I came across your profile and was impressed by your background in React. We’re looking for a Frontend Developer and thought you’d be a great fit…”

All without writing a single word.

---

## 🛠️ How to Run Locally

1. Clone the repo  
2. Create a `.env` file using the template below  
3. Install dependencies:
```bash
pip install -r requirements.txt

# Start the app
uvicorn main:app --reload

# Send a test email
curl -X POST http://localhost:8000/send_email/ \
-H "Content-Type: application/json" \
-d '{
  "recipient": "someone@example.com",
  "candidate_name": "Alex",
  "role": "Software Engineer",
  "company": "TechCorp",
  "recruiter_name": "John"
}'

---

## 📤 Sample Output

Hi Alex,

I’m Samantha from TechCorp. I came across your profile and was really impressed by your background in React and frontend development. We're currently hiring for a Frontend Developer role, and based on your experience, I think you'd be a great fit.

Would love to connect if you're open to chatting more!

Warm regards,
Samantha

---

## ⚠️ Disclaimer

This is a simplified, open-source version of an internal project built as part of a larger AI automation platform (AutoMiro).  
Some features have been removed for public demonstration.

---

## 🙌 Built By

Created by **Amir Abdel Nour** — AI Automation Engineer  
🔗 [LinkedIn](https://www.linkedin.com/in/amirabdelnour/)  
📫 [miroamir422@gmail.com](mailto:miroamir422@gmail.com)
