**Simple Readme for GeoCoder Project**

There is a Requirements.txt file, this should contain all dependencies that 
need to be installed locally,

**Kernel version :** _Python 3.6.0_

**Note:** _Settings has DEBUG = True_

In the settings file, at line 4, you will notice a variable called
API_KEY = "INSERT YOUR SECRET KEY HERE"

This is where you will put your Google API key.

I have embed simple google maps on both the Geocode and Reverse Geocode results pages.  They don't utilize the API KEY.

The site allows you to register as a user, login, logout, recover lost password (console email only with reset token)

There is a rudimentary Profile / Dashboard page, you can change your password and or edit your Profile information.

There are several main pages: 

1. Get Geocode -- Type is a valid address or location, returns latitude and longitude for location.

2. Reverse Geocode -- Enter valid latitude and longitude, returns location or address if it exists

3. Geocode Distance -- Enter in a pair of locations by latitude and longitude and choose metric or standard measure, return simple straight line distance in either meters or yards.

4. Address Distance -- Enter in two addresses or location names, choose metric or standard, returns simple straight line distance between locations in either meters or yards.

