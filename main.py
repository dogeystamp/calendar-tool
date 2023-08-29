from ics import Calendar, Event
import arrow
import datetime
import yaml

with open("config.yml") as f:
    conf = yaml.safe_load(f.read())

subjects = conf["subjects"]
vacation_days = conf["vacation_days"]
start_date = conf["start_date"]
end_date = conf["end_date"]
schedule_slots = conf["schedule_slots"]
schedule = conf["schedule"]

step = datetime.timedelta(days = 1)
# cycle-day (e.g. 1-6)
day = 1

cal = Calendar()

current_date = start_date

while current_date <= end_date:
    have_school = True
    # Vacations
    for vacation in vacation_days:
        if(not vacation.get("single")):
            if current_date >= vacation["start"] and current_date <= vacation["end"]:
                have_school = False
                break
        else:
            if current_date == vacation["single"]:
                have_school = False
                break
    # Weekends
    if current_date.weekday() == 5 or current_date.weekday() == 6:
        have_school = False

    if not have_school:
        current_date += step
        continue

    day_classes = schedule[day]["classes"]

    slot_idx = 0
    for subject_idx, sched_subject in enumerate(day_classes):
        subject_id = sched_subject["id"]
        subject_loc = sched_subject["loc"]
        is_short = sched_subject.get("short", False)

        subject = subjects[subject_id]

        start_time = schedule_slots[slot_idx]["start"]
        end_time = schedule_slots[slot_idx]["end"]

        slot_idx += 1
        if slot_idx >= len(schedule_slots):
            slot_idx = len(schedule_slots) - 1

        if not is_short:
            end_time = schedule_slots[slot_idx]["end"]
            slot_idx += 1

        ev = Event()
        ev.begin = arrow.get(f"{current_date} {start_time}", tzinfo="local")
        ev.end = arrow.get(f"{current_date} {end_time}", tzinfo="local")
        ev.location = str(subject_loc)
        ev.description = f"Day {day}, {subject_loc}"
        ev.name = subjects[subject_id]["name"]
        cal.events.add(ev)

    day += 1
    if day > len(schedule):
        day = 1

    current_date += step

with open("cal.ics", "w") as f:
    f.writelines(cal.serialize_iter())
