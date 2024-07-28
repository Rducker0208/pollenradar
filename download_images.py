import datetime
import os
import shutil
import requests

from split_image import split_image


# wo - 03:08 - per uur:
# https://image.buienradar.nl/2.0/image/sprite/WeatherMapPollenRadarHourlyNL?width=820&height=988&ak=45f6b15cdf98478fbf31aca23cbec6fe

# do - 00:02 - per uur:
# https://image.buienradar.nl/2.0/image/sprite/WeatherMapPollenRadarHourlyNL?width=820&height=988&ak=45f6b15cdf98478fbf31aca23cbec6fe

# wo - meerdags
# https://image.buienradar.nl/2.0/image/sprite/WeatherMapPollenRadarNL?width=372&height=396


def check_last_login() -> None:
    """Check time since the last user login to check if new maps need to be downloaded"""

    # current_time = str(datetime.datetime.now().time())[:5]
    current_time = str(datetime.datetime.now())
    date, time = current_time.split()

    # // get last user login from text file
    with open('last_login.txt') as x:
        last_login_time, last_login_date = x.read().split('_')

    # // set current time as latest login
    with open('last_login.txt', 'w') as x:
        x.write(f'{time}_{date}')

    # // download new maps if needed
    if last_login_time[0:2] != time[0:2]:
        get_hourly_maps()

    if date != last_login_date:
        get_daily_maps()


def get_hourly_maps() -> None:
    """Download hourly pollenmap from buienradar and split it into 24 hourly maps"""

    # // clear and create directory for the 24 maps
    shutil.rmtree('pollen_maps_daily')
    os.mkdir('pollen_maps_daily')

    # // download image using urllib
    url = (
        'http://image.buienradar.nl/2.0/image/sprite/WeatherMapPollenRadarHourlyNL?width=820&height=988&ak'
        '=45f6b15cdf98478fbf31aca23cbec6fe')

    r = requests.get(url, stream=True, verify=False)
    with open('pollenmap.png', 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)

    # // use a library called split_image to turn the image sheet into 24 seperate maps
    split_image(r'./pollenmap.png', 1, 24,
                False, True, False, 'pollen_maps_daily')


def get_daily_maps() -> None:
    """Download weekly pollenmap from buienradar and split it into 4 daily maps"""

    # // clear and create directory for the 5 maps
    shutil.rmtree('pollen_maps_weekly')
    os.mkdir('pollen_maps_weekly')

    # // download image using urllib
    url = 'https://image.buienradar.nl/2.0/image/sprite/WeatherMapPollenRadarNL?width=820&height=988'

    r = requests.get(url, stream=True, verify=False)
    with open('pollenmap_weekly.png', 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)

    # // use a library called split_image to turn the image sheet into 5 seperate maps, the first one is not used
    split_image(r'./pollenmap_weekly.png', 1, 5,
                False, True, False, 'pollen_maps_weekly')