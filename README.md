# calendar-tool

Tool to manage 6-day cyclic schedules for school.
The schedule shifts every week since there are only 5 weekdays,
and it also shifts every time there is a long weekend or other break.
calendar-tool takes all these disruptions into account over the course of the year.

Takes a YAML configuration file, and saves the calendar as ICS, to be imported in Google Calendar or other calendars that can support it.
