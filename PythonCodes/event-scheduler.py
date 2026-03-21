import logging
import datetime

logging.basicConfig(filename='PythonCodes/event-reminder.log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG,
                    filemode='a')


logger = logging.getLogger()

# Function to check for reminders
def check_event_reminder(events, current_time):
    for event in events:
        event_time = event['time']
        # Check if event is today or tomorrow
        time_difference = event_time - current_time
        if time_difference.days == 0 and time_difference.seconds <= 1800:  # Event in the next 30 minutes
            logging.info(f"Reminder sent for '{event['name']}' at {event_time}.")
            print(f"Reminder: Your '{event['name']}' is scheduled for today at {event_time.strftime('%I:%M %p')}. Please be ready.")
        elif time_difference.days == 1:  # Event tomorrow
            logging.info(f"Reminder scheduled for '{event['name']}' tomorrow at {event_time}.")
            print(f"Reminder: Your '{event['name']}' is scheduled for tomorrow at {event_time.strftime('%I:%M %p')}. Don't forget!")

# Function to schedule events
def schedule_event(name, event_date, event_time):
    event_datetime = datetime.datetime.combine(event_date, event_time)
    return {'name': name, 'time': event_datetime}

# Input events
events = [
    schedule_event("Team Meeting", datetime.date(2023, 12, 25), datetime.time(10, 0)),
    schedule_event("Project Presentation", datetime.date(2023, 12, 26), datetime.time(14, 0)),
    schedule_event("Doctor Appointment", datetime.date(2023, 12, 24), datetime.time(15, 0)),
]

current_time = datetime.datetime(2023, 12, 24, 14, 30)

for event in events:
    logger.info(f"Event '{event['name']}' schedule for {event['time']}")

check_event_reminder(events, current_time)
