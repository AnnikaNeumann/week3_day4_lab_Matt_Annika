from app import app
from flask import render_template
from modules.events_list import event_list

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=event_list)