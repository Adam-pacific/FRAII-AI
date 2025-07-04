import smtplib
from email.message import EmailMessage
import os

def send_report_email(receiver_email, subject, message, file_path=None):
    try:
        # Your Gmail credentials
        sender_email = "yadamahamed953@gmail.com"
        app_password = "mnsn ygxs hkmr rqew"

        # Create email
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg.set_content(message)

        # Attach a file if given
        if file_path:
            with open(file_path, "rb") as f:
                file_data = f.read()
                file_name = os.path.basename(file_path)
                maintype, subtype = "application", "octet-stream"
                msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=file_name)

        # Send email via Gmail
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)

        return "✅ Email with attachment sent successfully!"

    except Exception as e:
        return f"❌ Email failed: {e}"
