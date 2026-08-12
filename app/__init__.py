import os
from flask import Flask

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = os.getenv("FLASK_SECRET_KEY", "change-this-secret-key")

from app import routes_home, routes_portfolio
