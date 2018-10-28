from django.shortcuts import render

# Create your views here.
from geomapit.forms import GeoCodeForm, GeoMapForm


def geocode(request):

    if request.method == 'POST':
        form = GeoCodeForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            dummy = 99

    else:
        form = GeoCodeForm()

    return render(request, 'geocode.html', {'form': form})


def geomapit(request):

    if request.method == 'POST':
        form = GeoMapForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            dummy = 99

    else:
        form = GeoMapForm()

    return render(request, 'geomapit.html', {'form': form})
