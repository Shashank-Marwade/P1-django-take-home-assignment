import logging
import math
from django.http import HttpResponse
from django.template import loader
import pandas as pd

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

def query_csv(request):
    if 'latitude' in request.GET and 'longitude' in request.GET:
        df = pd.read_csv('FoodTruckLocator/food-truck-data.csv', dtype={'dayshours': str})
        user_lat = float(request.GET['latitude'])
        user_lon = float(request.GET['longitude'])
        df['Distance'] = df.apply(lambda row: haversine(user_lat, user_lon, row['Latitude'], row['Longitude']), axis=1)

        nearest_df = df.sort_values(by='Distance').head(10)
        context = {
            'locations': nearest_df.to_dict(orient='records')
        }

        template = loader.get_template('results.html')
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('map.html')
        return HttpResponse(template.render({}, request))
