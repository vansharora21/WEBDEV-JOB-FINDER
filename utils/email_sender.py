import smtplib
from email.message import EmailMessage

def send_email(sender, password, to, subject, body):
    try:
        msg = EmailMessage()
        msg["From"] = sender
        msg["To"] = to
        msg["Subject"] = subject
        msg.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
            
    except smtplib.SMTPAuthenticationError as e:
        print(f"\n⚠️ Gmail authentication failed!")
        print("❌ Make sure you're using a Gmail App Password, not your regular password.")
        print("Steps to fix:")
        print("1. Enable 2FA on your Google Account")
        print("2. Go to myaccount.google.com/apppasswords")
        print("3. Generate a 16-character app password")
        print("4. Update EMAIL_PASSWORD in .env with this password")
        print(f"\nError: {e}\n")
        raise
        
    except smtplib.SMTPException as e:
        print(f"❌ SMTP Error: {e}")
        raise
        
    except Exception as e:
        print(f"❌ Email sending failed: {e}")
        raise
