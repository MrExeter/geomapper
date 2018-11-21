# Exercise in GeoCoding  

_*** Requirements & Dependencies: ***_  

1. Install all packages listed in requirements.txt
2. Python 3.6.0
3. A valid Google Geocoding API Key  

Also, you will have to create either a PostgreSQL or SQLite3 database and make appropriate migrations and set passwords etc.

In the settings file, at line 4, you will notice a variable called
API_KEY = "INSERT YOUR SECRET KEY HERE" _(This is where you will put your Google API key.)_
 

1. Get Geocode -- Type is a valid address or location, returns latitude and longitude for location.
2. Reverse Geocode -- Enter valid latitude and longitude, returns location or address if it exists
3. Geocode Distance -- Enter in a pair of locations by latitude and longitude and choose metric or standard measure, return simple straight line distance in either meters or yards.
4. Address Distance -- Enter in two addresses or location names, choose metric or standard, returns simple straight line distance between locations in either meters or yards.

