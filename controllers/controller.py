from app import app
from flask import render_template, request
from modules.events_list import event_list, add_new_event
from modules.event import Event


@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=event_list)

@app.route('/event_form')
def event_form():
    return render_template('event_form.html', title="Event form")

@app.route('/event_form', methods=['POST'])
def add_task():
    new_event = Event(request.form['date'], request.form["event_name"], request.form["guest_number"], request.form["event_room"], request.form["description"])
    add_new_event(new_event)
    return render_template('event_form.html', title="Event form")