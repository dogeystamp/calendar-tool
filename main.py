import csv
import datetime
from config import *

step = datetime.timedelta(days = 1)
day = 1;
for i in range(offset):
    start_date += step


with open('calendar.csv', mode='w') as calendar:
    calendar_writer = csv.writer(calendar, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    calendar_writer.writerow(['Subject', 'Start Date', 'Start Time','End Date','End Time', 'All day event', 'Description' ,'Location'])

def period_to_time(start,period):
    if start:
        return start_times[period].strftime("%H:%M")

    else:
        return end_times[period].strftime("%H:%M")

def write_file(subject,date,long):
    with open('calendar.csv', mode='a') as calendar:
        calendar_writer = csv.writer(calendar, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        p2 = subject.period
        if long:
            p2 +=1
        calendar_writer.writerow([subject.name, str(date.month) + "/"+ str(date.day) + "/" +str(date.year), period_to_time(True,subject.period),str(date.month) + "/"+ str(date.day) + "/" +str(date.year),period_to_time(False,p2),"FALSE", day])

current_date = start_date-step

while True:
    current_date += step
    school = True;
    for vacation in vacation_days:
        if(len(vacation)>1):
            if current_date >= vacation[0] and current_date <= vacation[1]:
                school = False
                break
        else:
            if current_date == vacation[0]:
                school = False
                break
    if not school:
        continue
    if current_date > end_date:
        break
    if current_date.weekday() == 5 or current_date.weekday() == 6:
        continue
    schedule = schedule_dict[day]
    for period_order, period_id in enumerate(schedule):
        class_object = classes[period_id-1]
        class_object.period = period_order + 1
        long_period = False
        if period_order < len(schedule_dict) and schedule[period_order+1] == period_id and merge_periods:
            long_period = True
        if period_order > 0 and schedule[period_order-1] == period_id and merge_periods:
            continue
        write_file(class_object, current_date, long_period)
    day += 1
    if day > len(schedule_dict):
        day = 1
