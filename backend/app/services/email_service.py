import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.config import GMAIL_ADDRESS, GMAIL_APP_PASSWORD

def send_email(recipient, subject, body):
    """Send an email using Gmail SMTP."""
    try:
        msg = MIMEMultipart()
        msg['From'] = GMAIL_ADDRESS
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_ADDRESS, recipient, msg.as_string())
        server.quit()

        return {"message": "Email sent successfully!"}
    except Exception as e:
        return {"error": f"Failed to send email: {str(e)}"}

# Optional: Local test
if __name__ == "__main__":
    print(f"Sending test email from: {GMAIL_ADDRESS}")
    result = send_email(
        recipient="your-second-email@example.com",
        subject="🔥 AutoMiro Email Test",
        body="This is a test email sent from your AI email automation system. Let’s gooo!"
    )
    print(result)
