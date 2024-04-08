from django.shortcuts import render

gear = [
    {'brand': 'Fender',
     'make': 'Precision',
     'type': 'Bass',
     'model': 'Professional Series II',
     'colour': 'Olive Green'
     },
    {'brand': 'Fender',
     'make': 'Jazz',
     'type': 'Bass',
     'model': 'Marcus Miller Signature',
     'colour': 'Brown and Black'
     },
    {'brand': 'Fender',
     'make': 'Jazzmaster',
     'type': 'Electric Guitar',
     'model': 'J Mascis Signature',
     'colour': 'Gold and Cream'
     },
    {'brand': 'Fender',
     'make': 'Stratocaster',
     'type': 'Electric Guitar',
     'model': 'Unknown',
     'colour': 'Cream'
     }
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gear_index(request):
    return render(request, 'gear/index.html', {
        'gear': gear
    })