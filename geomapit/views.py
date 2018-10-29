'''
Description - Geomapit & Geocoding Views
@author - John Sentz
@date - 29-Oct-2018
@time - 10:40 AM
'''

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from geomapit.forms import GeoCodeForm, GeoMapForm, GeoDistanceForm, GeoDistanceAddressForm
from geomapit.utils import GeoCoder


@login_required
def geodistance_address(request):

    if request.method == 'POST':
        form = GeoDistanceAddressForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            address_1 = cd.get('address_1')
            address_2 = cd.get('address_2')
            units = cd.get('units')

            ###################################################################
            #
            # Call Google API through Util class to get geocode information
            #
            latlng_1 = GeoCoder.get_geocode(address_1)
            latlng_2 = GeoCoder.get_geocode(address_2)

            first_point_ok = latlng_1.get('latitude') is not None and latlng_1.get('longitude') is not None
            second_point_ok = latlng_2.get('latitude') is not None and latlng_2.get('longitude') is not None

            if first_point_ok and second_point_ok:
                ###############################################################
                # Both coordinates found, calculate distance between them
                #
                coordinate_pair = {
                    'latitude_1': latlng_1.get('latitude'),
                    'longitude_1': latlng_1.get('longitude'),
                    'latitude_2': latlng_2.get('latitude'),
                    'longitude_2': latlng_2.get('longitude')
                }
                units = {'units': units}

                # Get actual distance
                distance = GeoCoder.distance_between_points(coordinate_pair, units)
                distance = '{:,.2f}'.format(distance)

                # Set units for display
                if units.get('units') == '1':
                    unit_str = 'Meters'
                else:
                    unit_str = 'Yards'

                messages.success(request, "Distance found")
                context = {
                    'address_1': address_1,
                    'address_2': address_2,
                    'distance': distance,
                    'units': unit_str
                }

                return render(request, 'address_distance.html', context=context)

            else:
                form = GeoDistanceAddressForm()
                messages.error(request, 'Distance could not be calculate, address invalid!')
                return render(request, 'address_distance_form.html', {'form': form})

        else:
            return render(request, 'address_distance_form.html', {'form': form})

    else:
        form = GeoDistanceAddressForm()
        return render(request, 'address_distance_form.html', {'form': form})


@login_required
def geodistance_geocode(request):

    if request.method == 'POST':
        form = GeoDistanceForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            units = cd.get('units')

            coordinate_pair = {
                'latitude_1': cd.get('latitude_1'),
                'longitude_1': cd.get('longitude_1'),
                'latitude_2': cd.get('latitude_2'),
                'longitude_2': cd.get('longitude_2')
            }
            units = {'units': units}

            # Get actual distance
            distance = GeoCoder.distance_between_points(coordinate_pair, units)
            distance = '{:,.2f}'.format(distance)

            # Set units for display
            if units.get('units') == '1':
                unit_str = 'Meters'
            else:
                unit_str = 'Yards'

            messages.success(request, "Distance found")
            context = {
                'latitude_1': coordinate_pair.get('latitude_1'),
                'longitude_1': coordinate_pair.get('longitude_1'),
                'latitude_2': coordinate_pair.get('latitude_2'),
                'longitude_2': coordinate_pair.get('longitude_2'),
                'distance': distance,
                'units': unit_str
            }

            return render(request, 'geocode_distance.html', context=context)

        else:
            form = GeoDistanceForm()
            return render(request, 'geocode_distance_form.html', {'form': form})

    else:
        form = GeoDistanceForm()
        return render(request, 'geocode_distance_form.html', {'form': form})


@login_required
def geocode(request):

    if request.method == 'POST':

        form = GeoCodeForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            address = cd.get('address')
            ###################################################################
            #
            # Call Google API through Util class to get geocode information
            #
            latlng = GeoCoder.get_geocode(address)

            if latlng.get('latitude') is not None and latlng.get('longitude') is not None:
                context = latlng
                context['address'] = address.title()
                messages.success(request, "Geocode found")
                return render(request, 'geocode_result.html', context=context)
            else:
                form = GeoCodeForm()
                messages.error(request, 'Geocode not found or address invalid!')
                return render(request, 'geocode_form.html', {'form': form})
        else:
            return render(request, 'geocode_form.html', {'form': form})
    else:
        form = GeoCodeForm()
        return render(request, 'geocode_form.html', {'form': form})


@login_required
def geomapit(request):

    if request.method == 'POST':
        form = GeoMapForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            context = {'latitude': cd.get('latitude'), 'longitude': cd.get('longitude')}

            ###################################################################
            #
            # Call Google API through Util class to get location based on lat, lng
            #
            address = GeoCoder.get_reverse_geocode(context)

            if address == 'No address found':
                form = GeoMapForm()
                messages.error(request, "No address or location found")
                return render(request, 'geomapit_form.html', {'form': form})
            else:
                context['address'] = address
                messages.success(request, "Address or location found")
                # Call utils api calls with address, context will either be lat, lon or an error message
                return render(request, 'geomapit_result.html', context=context)
        else:
            return render(request, 'geomapit_form.html', {'form': form})

    else:
        form = GeoMapForm()
        return render(request, 'geomapit_form.html', {'form': form})
