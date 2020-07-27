# United Energy EnergyEasy API

This is an API implementation to access personal electricity usage data from the [United Energy website](https://energyeasy.ue.com.au/).   

## Potential Uses
- Get data every data with a cron job
- Display live electricity usage

## Set Up
1. Have a United Energy account (email and password)
2. Install requests with `pip install requests` or use `poetry shell` 

## Example Code (using [UnitedEnergy.py](https://github.com/Blake-Haydon/United-Energy-EnergyEasy-API-unofficial-/blob/master/UnitedEnergy.py))
Authenticate with your email and password by creating an object
```
import UnitedEnergy
ue_api = UnitedEnergy.API(<email>, <password>)
```
\
Get data for the day, 30 days ago
```
ue_api.day_data(30)
```
\
Get data for the week, 3 weeks ago
```
ue_api.week_data(3)
```
\
Get data for the month, 15 months ago
```
ue_api.month_data(15)
```
\
Get data for this year _(0 = current)_
```
ue_api.year_data(0)
```
\
Get daily usage data for 15/3/2020
```
import datetime
on_date_data(datetime.date(2020, 3, 15))
```