'''
Description - Geocode URLS
@author - John Sentz
@date - 06-Nov-2018
@time - 1:32 PM
'''

from django.urls import path

from . import views

urlpatterns = [
    path('geocode/', views.geocode, name='geocode'),
    path('geomapit/', views.geomapit, name='geomapit'),
    path('geodistance_address/', views.geodistance_address, name='geodistance_address'),
    path('geodistance_geocode/', views.geodistance_geocode, name='geodistance_geocode'),
]
