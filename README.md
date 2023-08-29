# calendar-tool

Tool to manage 6-day cyclic schedules for school.
The schedule shifts every week since there are only 5 weekdays,
and it also shifts every time there is a long weekend or other break.
calendar-tool takes all these disruptions into account over the course of the year.

Takes a YAML configuration file, and saves the calendar as ICS, to be imported in Google Calendar or other calendars that can support it.

## usage

- Clone repo:
    ```
    git clone https://github.com/dogeystamp/calendar-tool
    cd calendar-tool
    ```

- Copy `config.example.yml` to `config.yml`:
    ```
    cp config.example.yml config.yml
    ```

- Edit the configuration (the comments and examples should explain everything):
    ```
    vim config.yml
    ```

- Run the script:
    ```
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python3 main.py
    ```

- Your calendar should now be in `cal.ics`.
