import os
import smtplib
from email.message import EmailMessage
from flask import render_template, request, redirect, url_for, flash, abort
from app import app


def get_profile():
    return {
        "name": "Esona Mzalazala",
        "title": "BSc Teaching Graduate | Emerging Education Professional",
        "headline": "Shaping confident learners with creative lesson design and inclusive classroom leadership.",
        "bio": [
            "Recent BSc Teaching graduate with strong experience in curriculum planning, classroom culture, and student-centered instruction.",
            "I design engaging learning experiences that honor diversity, encourage curiosity, and build meaningful academic progress.",
            "Focused on blending evidence-based pedagogy with digital tools to support every student's growth." 
        ],
        "specialties": [
            "Differentiated lesson design",
            "Inclusive classroom strategies",
            "Assessment & reflective teaching",
            "Learning technology integration"
        ],
        "experience": [
            {
                "role": "Student Teacher",
                "organization": "Riverstone Academy",
                "dates": "Jan 2024 - Jun 2024",
                "details": "Led interdisciplinary units in literacy and science, building strong learner engagement through cooperative inquiry and student reflection."
            },
            {
                "role": "Teaching Assistant",
                "organization": "Learning Lab Institute",
                "dates": "Jul 2023 - Dec 2023",
                "details": "Supported differentiated instruction, tracked student progress, and collaborated with teachers to strengthen classroom routines and formative assessment."
            }
        ],
        "education": [
            {
                "degree": "BSc in Teaching",
                "institution": "State University of Education",
                "dates": "2024"
            }
        ],
        "projects": [
            {
                "slug": "inclusive-stem-curriculum",
                "name": "Inclusive STEM Curriculum",
                "description": "Designed an accessible, inquiry-based unit that invited learners to investigate real-world problems and reflect on their own learning process.",
                "detail": "This project guided students through an interactive STEM inquiry cycle, using hands-on experiments and reflective writing to build strong conceptual understanding and academic confidence.",
                "highlights": [
                    "Designed differentiated learning pathways for diverse learners.",
                    "Used formative reflections to fuel student growth.",
                    "Connected science concepts to real-world challenges."
                ]
            },
            {
                "slug": "digital-classroom-hub",
                "name": "Digital Classroom Hub",
                "description": "Created a student-centered digital hub for formative feedback, portfolios, and family communication to support continuous learning.",
                "detail": "This project developed a classroom hub where students showcased learning artifacts, families received updates, and teachers shared real-time progress to strengthen home-school partnerships.",
                "highlights": [
                    "Built an accessible portfolio workflow for student reflection.",
                    "Improved engagement with consistent family communication.",
                    "Supported data-informed planning through formative tracking."
                ]
            }
        ],
        "contact": {
            "email": "esona.mzalazala@example.com",
            "linkedin": "linkedin.com/in/esona-mzalazala",
            "portfolio": "esona-teachfolio.com"
        }
    }


def get_lessons():
    return [
        {
            "title": "Inquiry-based Literacy Studio",
            "description": "A reading and writing workshop that connected storytelling, research, and peer collaboration to deepen literacy confidence."
        },
        {
            "title": "STEAM Exploration Lab",
            "description": "A hands-on science unit that encouraged student investigation, hypothesis testing, and creative presentation through classroom engineering challenges."
        },
        {
            "title": "Digital Learning Showcase",
            "description": "A blended learning sequence where learners used digital tools to document progress, reflect on growth, and present learning products."
        }
    ]


def get_testimonials():
    return [
        {
            "quote": "Esona brings warmth, structure, and a thoughtful spirit to every lesson. Their planning is always grounded in student voice.",
            "author": "Mentor Teacher, Riverstone Academy"
        },
        {
            "quote": "A strong collaborator who adapts quickly and builds trust with learners. Esona’s classroom environment is welcoming and ambitious.",
            "author": "Instructional Coach, Learning Lab Institute"
        }
    ]


def get_project(slug):
    profile = get_profile()
    return next((project for project in profile["projects"] if project["slug"] == slug), None)


@app.route("/project/<slug>")
def project_detail(slug):
    profile = get_profile()
    project = get_project(slug)
    if not project:
        abort(404)
    return render_template("project_detail.html", profile=profile, project=project)


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


@app.route("/")
def home():
    profile = get_profile()
    return render_template("index.html", profile=profile)


@app.route("/lessons")
def lessons():
    profile = get_profile()
    lessons = get_lessons()
    testimonials = get_testimonials()
    return render_template("lessons.html", profile=profile, lessons=lessons, testimonials=testimonials)


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
        flash("Your message was sent successfully. I’ll follow up soon.")
    except Exception as exc:
        app.logger.error("Contact form error: %s", exc)
        flash("Your message was received, but email delivery is not configured. Please contact directly if the issue persists.")

    return redirect(url_for("home"))
