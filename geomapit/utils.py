'''
Description - Utility Class for making Google Geo Coding API calls
@author - John Sentz
@date - 29-Oct-2018
@time - 10:41 AM
'''

from math import sin, cos, sqrt, atan2, radians

import googlemaps
import json
import requests

from chanfact.settings import API_KEY

EARTH_RADIUS_METERS = 6.731 * 10 ** 6
EARTH_RADIUS_YARDS = 7.3611 * 10 ** 6
BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json?"


class GeoCoder:
    """GeoCoder Class"""

    @classmethod
    def distance_between_points(cls, coordinate_pair, units):
        """
        Function to calculate the simple 'straight' line path between two points on a sphere
        :param coordinate_pair: - Dictionary wotj two coordinate pairs described in lats and longs
        :param units: - Specifies whether metric (meters) of standard (yards)
        :return: - The distance between the two coordinates on he surface of a sphere.
        """
        lat_1 = coordinate_pair.get('latitude_1')      # Access the individual lat, lon values
        lon_1 = coordinate_pair.get('longitude_1')

        lat_2 = coordinate_pair.get('latitude_2')
        lon_2 = coordinate_pair.get('longitude_2')

        """
        The following is a calculation based on the Haversine Formula.
        It calculates the simple distance between two points on the surface
        of a sphere, given the lat and lon angles of each point.
        """
        lat_radians_1 = radians(lat_1)      # Convert all angles from degrees to radians
        lat_radians_2 = radians(lat_2)

        delta_lats = radians(lat_2 - lat_1)
        delta_lons = radians(lon_2 - lon_1)

        the_a = sin(delta_lats / 2) ** 2 + cos(lat_radians_1) * cos(lat_radians_2) * sin(delta_lons / 2) ** 2
        the_c = 2 * atan2(sqrt(the_a), sqrt(1 - the_a))

        if units.get('units') == '1':
            earth_radius = EARTH_RADIUS_METERS
        else:
            earth_radius = EARTH_RADIUS_YARDS

        the_distance = earth_radius * the_c

        return the_distance

    @classmethod
    def get_geocode(cls, address):
        """
        Function to call Google Geocode API and return lat and long for a given address location
        :param address:  String value of location or place, e.g., full street address, landmark etc.
        :return:  Dictionary containing the lat and long for the given location if it exists, else returns
        NONE values
        """
        gmaps_key = googlemaps.Client(key=API_KEY)
        geocode_result = gmaps_key.geocode(address)

        try:
            lat = geocode_result[0]["geometry"]["location"]["lat"]
            lon = geocode_result[0]["geometry"]["location"]["lng"]

        except:
            lat = None
            lon = None

        return {"latitude": lat, "longitude": lon}

    @classmethod
    def get_reverse_geocode(cls, latlng):
        """
        Function to call Google Geocode API and returns the nearest street address for a given lat and long
        :param latlng: A tuple with two values, the latitude and the longitude
        :return: The formatted address, if it exists.
        """

        params = "latlng={lat},{lon}&key={key}".format(
            lat=latlng.get('latitude'),
            lon=latlng.get('longitude'),
            key=API_KEY
        )

        url = "{base}{params}".format(base=BASE_URL, params=params)
        response = requests.get(url)
        data = json.loads(response.text)
        if data["status"] == 'OK':
            found_address = data['results'][1]['formatted_address']
        else:
            found_address = 'No address found'

        return found_address
