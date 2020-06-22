import requests
import json
import time
import datetime


class API:
    """
    This unofficial API allows for electricity usage data to be fetched from the United Energy EnergyEasy site.

    self.requests_session = requests session that stores authentication cookie
    """

    def __init__(self, email: str, password: str) -> None:
        LOGIN_URL = "https://energyeasy.ue.com.au/login/index/login_security_check"

        # Initalise request session that stores the authentication cookie within the object
        self.requests_session = requests.Session()

        # Login requires the email and password to be sent to the LOGIN_URL
        payload = {
            "login_email": email,
            "login_password": password,
        }

        self.requests_session.post(
            LOGIN_URL,
            data=payload
        )

    def _fetch_data(self, time_period: str, time_ago: int) -> dict:
        """ Returns a dictionary containing the data from a time_period with some number of time_ago. Time periods can
        be day, week, month, season and year. """

        unix_time = int(time.time())
        data_url = f"https://energyeasy.ue.com.au/electricityView/period/{time_period}/{time_ago}?_{unix_time}"
        print(data_url)
        result = self.requests_session.get(data_url)
        return json.loads(result.text)

    def day_data(self, days_ago: int) -> dict:
        """ Returns a dictionary containing the data from some number of days_ago. The number of days_ago >= 0. """
        TIME_PERIOD = "day"
        return self._fetch_data(TIME_PERIOD, days_ago)

    def week_data(self, weeks_ago: int) -> dict:
        """ Returns a dictionary containing the data from some number of weeks_ago. The number of weeks_ago >= 0. """
        TIME_PERIOD = "week"
        return self._fetch_data(TIME_PERIOD, weeks_ago)

    def month_data(self, months_ago: int) -> dict:
        """ Returns a dictionary containing the data from some number of months_ago. The number of months_ago >= 0. """
        TIME_PERIOD = "month"
        return self._fetch_data(TIME_PERIOD, months_ago)

    def year_data(self, years_ago: int) -> dict:
        """ Returns a dictionary containing the data from some number of years_ago. The number of years_ago >= 0. """
        TIME_PERIOD = "year"
        return self._fetch_data(TIME_PERIOD, years_ago)

    def season_data(self, seasons_ago: int) -> dict:
        """ Returns a dictionary containing the data from some number of seasons_ago. The number of seasons_ago >= 0. """
        TIME_PERIOD = "season"
        return self._fetch_data(TIME_PERIOD, seasons_ago)

    def on_date_data(self, past_date: datetime.date) -> dict:
        """ Returns a dictionary containing the data from a past_data. The past_date must be in the past or today. """
        today = datetime.date.today()

        # Calculate the number of days ago the date is
        date_delta = today - past_date
        days_ago = date_delta.days
        return self.day_data(days_ago)
