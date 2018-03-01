from django.shortcuts import render
import requests
# Create your views here.


def home(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR','')

    response = requests.get('http://freegeoip.net/json/%s' % ip_address)
    geodata = response.json()
    return  render(request, 'index.html',{
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'cc': geodata['country_code'],
        'time_zone': geodata['time_zone'],
        'latitude' : geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key' : 'AIzaSyCDJRm6YzyDeX4MeEMN101U2GXEPbzP7Ms'
    })