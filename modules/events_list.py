from modules.event import Event

event1 = Event("03/04/2022", "Queen", 30000, "Murrayfield stadium", "Best concert ever also impossible",True)
event2 = Event("05/06/2022", "Iron maiden", 25000, "Hydro", "It's Iron Maiden what else do you need?", False)
event3 = Event("23/072022",  "Michael Jackson", 27000, "Arthur's Seat", "Imprison him after the concert please", False)
event4 = Event("12/08/2022", "Ghost", 15000, "some pub", "It's a good band people", True)
event_list = [event1, event2, event3, event4]

def add_new_event(event):
    event_list.append(event)

def delete_selected(event):
    event_list.remove(event)