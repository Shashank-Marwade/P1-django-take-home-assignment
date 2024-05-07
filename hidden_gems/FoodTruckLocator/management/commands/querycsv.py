from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from FoodTruckLocator.views import haversine

class Command(BaseCommand):
    help = 'Queries the CSV for nearby food trucks based on given latitude and longitude'

    def add_arguments(self, parser):
        parser.add_argument('latitude', type=float, help='Latitude of the user location')
        parser.add_argument('longitude', type=float, help='Longitude of the user location')

    def handle(self, *args, **kwargs):
        latitude = kwargs['latitude']
        longitude = kwargs['longitude']

        try:
            df = pd.read_csv('FoodTruckLocator/food-truck-data.csv', dtype={'dayshours': str})
            df['Distance'] = df.apply(lambda row: haversine(latitude, longitude, row['Latitude'], row['Longitude']), axis=1)

            nearest_df = df.sort_values(by='Distance').head(10)
            if nearest_df.empty:
                self.stdout.write(self.style.SUCCESS('No nearby food trucks found.'))
            else:
                for index, row in nearest_df.iterrows():
                    self.stdout.write(f"{row['Applicant']}, {row['Address']}, {row['Distance']:.2f} km")

        except FileNotFoundError:
            raise CommandError('Food truck data file not found.')
