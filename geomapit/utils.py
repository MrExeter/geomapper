import googlemaps
from chanfact.settings import API_KEY
import requests
import json
from math import sin, cos, sqrt, atan, atan2, radians

EARTH_RADIUS_METERS = 6.731 * 10 ** 6
EARTH_RADIUS_YARDS = 7.3611 * 10 ** 6
BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json?"


class GeoCoder:

    @classmethod
    def distance_between_points(cls, point_1, point_2, units):
        """
        :param point_1: - A tuple with the lat and lon for point_1
        :param point_2: - A tuple with the lat and lon for point_2
        :param units: - Specifies whether metric (meters) or standard (yards)
        :return: - The simple 'as the bird flies' distance in meters or yards
        """

        lat_1 = point_1[0]      # Access the individual lat, lon values
        lon_1 = point_1[1]

        lat_2 = point_2[0]
        lon_2 = point_2[1]

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

        if units == 'METRIC':
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
            lat=latlng[0],
            lon=latlng[1],
            key=API_KEY
        )

        url = "{base}{params}".format(base=BASE_URL, params=params)
        response = requests.get(url)
        data = json.loads(response.text)
        if data["status"] == 'OK':
            found_address = data['results'][0]['formatted_address']
        else:
            found_address = 'No address found'

        return found_address


# address = "271 East Bellevue Dr., Pasadena, CA 91101"
# my_geocode = GeoCoder.get_geocode(address)
# print(my_geocode)
#
# dummy=21
# address = GeoCoder.get_reverse_geocode((my_geocode.get("latitude"), my_geocode.get("longitude")))
# print(address)
# debug = 99
