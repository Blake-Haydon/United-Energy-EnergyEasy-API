# United Energy EnergyEasy API

> **Warning**
> This API has been deprecated by United Energy. It is no longer possible to access the data from the website. This API will no longer be maintained.

This is an API implementation to access personal electricity usage data from the [United Energy website](https://energyeasy.ue.com.au/).

## Potential Uses

- Get data every data with a cron job
- Display live electricity usage

## Set Up

1. Have a United Energy account (email and password)
2. Install via pip

```bash
pip install https://github.com/Blake-Haydon/United-Energy-EnergyEasy-API/blob/master/dist/united_energy-0.3.2-py3-none-any.whl?raw=true
```

## Update API

```bash
pip install https://github.com/Blake-Haydon/United-Energy-EnergyEasy-API/blob/master/dist/united_energy-0.3.2-py3-none-any.whl?raw=true --upgrade
```

## Example Code

```python
# Authenticate with your email and password
import united_energy
ue_api = united_energy.API(<email>, <password>)

# Refresh API data to most recent data
ue_api.refresh_data()

# Possible API Requests
ue_api.day_data(30)                             # Get data for the day, 30 days ago
ue_api.week_data(3)                             # Get data for the week, 3 weeks ago
ue_api.month_data(15)                           # Get data for the month, 15 months ago
ue_api.year_data(0)                             # Get data for this year (0 = current)
ue_api.on_date_data(datetime.date(2020, 3, 15)) # Get daily usage data for 15/3/2020
```
