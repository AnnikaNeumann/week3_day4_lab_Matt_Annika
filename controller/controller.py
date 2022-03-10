from app import app
from flask import render_template
from modules.events_list import events_list

@app.route("/events")
def index():
    return render_template('index.html', title="Home", events=events_list)