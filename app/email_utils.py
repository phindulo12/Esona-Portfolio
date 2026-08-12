import os
import smtplib
from email.message import EmailMessage


def send_contact_email(name, email, subject, message_body):
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    recipient = os.getenv("EMAIL_RECEIVER", sender)

    if not smtp_server or not sender or not password:
        raise RuntimeError("SMTP service is not configured.")

    email_message = EmailMessage()
    email_message["Subject"] = f"Portfolio Contact from {name}: {subject}"
    email_message["From"] = sender
    email_message["To"] = recipient
    email_message.set_content(
        f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message_body}\n"
    )

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(email_message)
