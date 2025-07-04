import smtplib
from email.mime.text import MIMEText

def send_report_email(recipient, subject, message):
    try:
        sender_email = "adamahamed953@gmail.com"
        app_password = "mnsn ygxs hkmr rqew"  # 16 chars, no spaces

        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()

        return "✅ Email sent successfully!"
    except Exception as e:
        return f"❌ Email failed: {e}"
