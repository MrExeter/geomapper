'''
Description - Geocoding Forms
@author - John Sentz
@date - 29-Oct-2018
@time - 10:35 AM
'''

from django import forms


class GeoCodeForm(forms.Form):

    address = forms.CharField(max_length=128, required=True)


class GeoMapForm(forms.Form):
    # Please Note, Google actually allows for +- 85 degrees plus a small fraction
    # for simplicity I have limited the range to +- 84, besides latitudes at these
    # extremes are well into either the Arctic or Antarctic
    latitude = forms.FloatField(min_value=-84.0, max_value=84.0)
    longitude = forms.FloatField(min_value=-180.0, max_value=180.0)


class GeoDistanceAddressForm(forms.Form):

    address_1 = forms.CharField(max_length=128, required=True)
    address_2 = forms.CharField(max_length=128, required=True)
    units = forms.ChoiceField(choices=((1, 'METRIC'), (2, 'STANDARD')))


class GeoDistanceForm(forms.Form):

    latitude_1 = forms.FloatField(min_value=-84.0, max_value=84.0)
    longitude_1 = forms.FloatField(min_value=-180.0, max_value=180.0)

    latitude_2 = forms.FloatField(min_value=-84.0, max_value=84.0)
    longitude_2 = forms.FloatField(min_value=-180.0, max_value=180.0)
    units = forms.ChoiceField(choices=((1, 'METRIC'), (2, 'STANDARD')))
