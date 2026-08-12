from flask import render_template, request, redirect, url_for, flash
from app import app
from app.data import get_profile
from app.email_utils import send_contact_email


@app.route("/")
def home():
    profile = get_profile()
    return render_template("index.html", profile=profile)


@app.route("/send-message", methods=["POST"])
def send_message():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    subject = request.form.get("subject", "Portfolio inquiry").strip()
    message_body = request.form.get("message", "").strip()

    if not name or not email or not message_body:
        flash("Please complete all fields before sending your message.")
        return redirect(url_for("home"))

    try:
        send_contact_email(name, email, subject, message_body)
        flash("Your message was sent successfully. I'll follow up soon.")
    except Exception as exc:
        app.logger.error("Contact form error: %s", exc)
        flash("Your message was received, but email delivery is not configured. Please contact directly if the issue persists.")

    return redirect(url_for("home"))
