from django.http import Http404
from django.shortcuts import render


# Ride types are fixed, so a plain list is enough (no database model needed).
RIDES = [
    {'slug': 'bike', 'name': 'Bike', 'seats': 1, 'price_per_km': 6, 'image': 'website/images/bike.png',
     'tagline': 'Beat the traffic', 'description': 'Quick and cheap rides for one person. Best for short trips in busy city traffic.'},
    {'slug': 'auto', 'name': 'Auto', 'seats': 3, 'price_per_km': 10, 'image': 'website/images/auto.png',
     'tagline': 'Everyday rides', 'description': 'Affordable auto-rickshaw rides for up to three people, no bargaining needed.'},
    {'slug': 'mini', 'name': 'Mini', 'seats': 4, 'price_per_km': 13, 'image': 'website/images/mini.png',
     'tagline': 'Compact and comfy', 'description': 'AC hatchbacks at a budget price. A comfortable choice for daily travel.'},
    {'slug': 'sedan', 'name': 'Sedan', 'seats': 4, 'price_per_km': 16, 'image': 'website/images/sedan.png',
     'tagline': 'Extra legroom', 'description': 'Spacious sedans with more boot space. Great for airport and long trips.'},
    {'slug': 'suv', 'name': 'SUV', 'seats': 6, 'price_per_km': 22, 'image': 'website/images/suv.png',
     'tagline': 'Room for everyone', 'description': 'Large SUVs for groups and families with plenty of luggage.'},
]


def get_ride(slug):
    for ride in RIDES:
        if ride['slug'] == slug:
            return ride
    raise Http404('Ride type not found')


def home(request):
    return render(request, 'website/home.html')


def rides(request):
    context = {
        'rides': RIDES,
        'pickup': request.GET.get('pickup', '').strip(),
        'drop': request.GET.get('drop', '').strip(),
    }
    return render(request, 'website/rides.html', context)


def ride_detail(request, slug):
    ride = get_ride(slug)
    others = [r for r in RIDES if r['slug'] != slug]
    return render(request, 'website/ride_detail.html', {'ride': ride, 'others': others})
