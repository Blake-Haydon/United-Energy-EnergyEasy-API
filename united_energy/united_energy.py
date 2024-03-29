import requests
import json
import time
import datetime


class API:
    """
    This unofficial API allows for electricity usage data to be fetched from the United Energy EnergyEasy site.

    `self.requests_session`: requests session that stores authentication cookie
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

        # Hard to raise an exception if the login fails as we receive a 200 response on failure
        self.requests_session.post(LOGIN_URL, data=payload)

    def _fetch_data(self, time_period: str, time_ago: int) -> dict:
        """Returns a dictionary containing the data from a time_period with some number of time_ago. Time periods can
        be day, week, month, season and year."""

        unix_time = int(time.time())
        data_url = f"https://energyeasy.ue.com.au/electricityView/period/{time_period}/{time_ago}?_{unix_time}"
        result = self.requests_session.get(data_url)
        return json.loads(result.text)

    def refresh_data(self) -> None:
        """Force refresh to get the most current data. The current day data may not be accurate (see website)."""
        latest_interval = self.day_data(0)["latestInterval"]
        unix_time = int(time.time())

        # I think this url checks if the data needs updating
        check_refresh_url = f"https://energyeasy.ue.com.au/electricityView/latestData?lastKnownInterval={latest_interval}&_={unix_time}"
        # I think this prompts the server to update its data
        real_refresh_url = f"https://energyeasy.ue.com.au/electricityView/isElectricityDataUpdated?lastKnownInterval={latest_interval}&_={unix_time}"

        # Run the request to see if the data needs to be updated
        res = self.requests_session.get(check_refresh_url)
        if res.json()["poll"] is True:
            self.requests_session.get(real_refresh_url)

    def day_data(self, days_ago: int) -> dict:
        """Returns a dictionary containing the data from some number of days_ago. The number of days_ago >= 0."""
        TIME_PERIOD = "day"
        return self._fetch_data(TIME_PERIOD, days_ago)

    def week_data(self, weeks_ago: int) -> dict:
        """Returns a dictionary containing the data from some number of weeks_ago. The number of weeks_ago >= 0."""
        TIME_PERIOD = "week"
        return self._fetch_data(TIME_PERIOD, weeks_ago)

    def month_data(self, months_ago: int) -> dict:
        """Returns a dictionary containing the data from some number of months_ago. The number of months_ago >= 0."""
        TIME_PERIOD = "month"
        return self._fetch_data(TIME_PERIOD, months_ago)

    def year_data(self, years_ago: int) -> dict:
        """Returns a dictionary containing the data from some number of years_ago. The number of years_ago >= 0."""
        TIME_PERIOD = "year"
        return self._fetch_data(TIME_PERIOD, years_ago)

    def season_data(self, seasons_ago: int) -> dict:
        """Returns a dictionary containing the data from some number of seasons_ago. The number of seasons_ago >= 0."""
        TIME_PERIOD = "season"
        return self._fetch_data(TIME_PERIOD, seasons_ago)

    def on_date_data(self, past_date: datetime.date) -> dict:
        """Returns a dictionary containing the data from a past_data. The past_date must be in the past or today."""
        today = datetime.date.today()

        # Calculate the number of days ago the date is
        date_delta = today - past_date
        days_ago = date_delta.days
        return self.day_data(days_ago)


if __name__ == "__main__":
    # Input real email and password to test the API
    email = "test_email"
    password = "test_password"
    ue_api = API(email, password)

    # Refresh API data to most recent data
    ue_api.refresh_data()

    # Get data from 5 days ago
    day_data = ue_api.day_data(5)
    print(day_data)
