from flask import render_template, abort
from app import app
from app.data import get_profile, get_lessons, get_testimonials, get_project


@app.route("/lessons")
def lessons():
    profile = get_profile()
    lessons = get_lessons()
    testimonials = get_testimonials()
    return render_template("lessons.html", profile=profile, lessons=lessons, testimonials=testimonials)


@app.route("/project/<slug>")
def project_detail(slug):
    profile = get_profile()
    project = get_project(slug)
    if not project:
        abort(404)
    return render_template("project_detail.html", profile=profile, project=project)
