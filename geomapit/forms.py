from django import forms


class GeoCodeForm(forms.Form):

    address = forms.CharField(max_length=128, required=True)


class GeoMapForm(forms.Form):

    latitude = forms.FloatField(min_value=-84.0, max_value=84.0)
    longitude = forms.FloatField(min_value=-180.0, max_value=180.0)
