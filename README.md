# AutoMiro: AI Recruitment Email Automation 💼📧

This is a custom AI-powered recruitment outreach tool — built as one of many automation services under the **AutoMiro** platform.

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
- Gmail SMTP (with secure App Passwords)
- Pydantic, smtplib, dotenv

---

## 📦 Example Use Case

Recruiter inputs:

- Candidate: *Alex Johnson*  
- Role: *Frontend Developer*  
- Company: *TechCorp*  
- Recruiter: *Samantha*

AutoMiro instantly generates and sends a personalized message like:

> “Hi Alex, I’m Samantha from TechCorp. I came across your profile and was impressed by your background in React. We’re looking for a Frontend Developer and thought you’d be a great fit…”

All without writing a single word.

---

## 🛠️ How to Run Locally

1. Clone the repo  
2. Create a `.env` file like this:


EMAIL_ADDRESS=you@gmail.com EMAIL_PASSWORD=your_app_password OPENAI_API_KEY=your_openai_key

go
Copy
Edit

3. Run the FastAPI app:

```bash
uvicorn main:app --reload
Test it:
bash
Copy
Edit
curl -X POST http://localhost:8000/send_email/ \
-H "Content-Type: application/json" \
-d '{
  "recipient": "someone@example.com",
  "candidate_name": "Alex",
  "role": "Software Engineer",
  "company": "TechCorp",
  "recruiter_name": "John"
}'
