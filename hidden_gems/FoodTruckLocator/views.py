from datetime import datetime
import logging
import math
import re
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import pandas as pd
from django.http import JsonResponse

logger = logging.getLogger(__name__)

def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0
    # Convert degrees to radians
    lat1_rad, lon1_rad, lat2_rad, lon2_rad = map(math.radians, [lat1, lon1, lat2, lon2])
    # Differences
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def time_to_24h(time_str):
    """Convert a time string with AM/PM to 24-hour format."""
    if 'PM' in time_str and not time_str.startswith('12'):  # Convert PM to 24-hour, except for 12 PM which is already correct
        return int(time_str.replace('PM', '')) + 12
    elif 'AM' in time_str and time_str.startswith('12'):  # Convert 12 AM to 00 hours
        return 0
    else:
        return int(time_str.replace('AM', '').replace('PM', ''))

def parse_dayshours(dayshours_str):
    # Check if the input is a string and not empty
    if not dayshours_str or not isinstance(dayshours_str, str):
        return "Closed"

    # Regular expression to extract day and time ranges
    pattern = r'([a-zA-Z]+)-([a-zA-Z]+):?([\dAPM]+)-([\dAPM]+)?/?([\dAPM]+)?-?([\dAPM]+)?/?([\dAPM]+)?-?([\dAPM]+)?'
    match = re.match(pattern, dayshours_str)
    # pattern = r'([MTWFS][ouehra][neduit]+)(?:-(\w+))?|([MTWFS][ouehra][neduit]+)(?:/([MTWFS][ouehra][neduit]+))*/:(\d{1,2}(?:AM|PM))-(\d{1,2}(?:AM|PM))(?:/(\d{1,2}(?:AM|PM))-(\d{1,2}(?:AM|PM)))*'
    # match = re.findall(pattern, dayshours_str)


    if not match:
        return "-"  # Return "-" if there's any error in parsing

    # Extract matched groups
    start_day, end_day, start_hour1, end_hour1, start_hour2, end_hour2, start_hour3, end_hour3 = match.groups()

    # Current time setup
    current_time = datetime.now()
    current_hour = current_time.hour
    current_weekday = current_time.strftime('%a')

    # Mapping days to weekday numbers
    day_mapping = {
        'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6
    }

    # Prepare time ranges to compare
    time_ranges = []
    for start_hour, end_hour in [(start_hour1, end_hour1), (start_hour2, end_hour2), (start_hour3, end_hour3)]:
        if start_hour and end_hour:  # Ensure both times are available
            time_ranges.append((time_to_24h(start_hour), time_to_24h(end_hour)))

    # Check if the current day and time are within any of the specified ranges
    if (day_mapping.get(start_day, -1) <= current_time.weekday() <= day_mapping.get(end_day, 7)) and \
            any(start <= current_hour < end for start, end in time_ranges):
        return "Open"
    else:
        return "Closed"

def query_csv(request):
    if 'latitude' in request.GET and 'longitude' in request.GET:
        df = pd.read_csv('FoodTruckLocator/food-truck-data.csv', dtype={'dayshours': str})
        user_lat = float(request.GET['latitude'])
        user_lon = float(request.GET['longitude'])
        df['Distance'] = df.apply(lambda row: haversine(user_lat, user_lon, row['Latitude'], row['Longitude']), axis=1)
        df['Status'] = df['dayshours'].apply(parse_dayshours)  # Apply the status function

        nearest_df = df.sort_values(by='Distance').head(10)
        context = {
            'locations': nearest_df.to_dict(orient='records')
        }

        template = loader.get_template('results.html')
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('map.html')
        return HttpResponse(template.render({}, request))
