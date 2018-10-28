from django.conf.urls import url
from . import views
from django.urls import path, include

urlpatterns = [
    path('geocode/', views.geocode, name='geocode'),
    path('geomapit/', views.geomapit, name='geomapit'),
]
