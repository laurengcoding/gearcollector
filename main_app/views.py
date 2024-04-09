from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Gear

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gear_index(request):
    gear = Gear.objects.all()
    return render(request, 'gear/index.html', {
        'gear': gear
    })

def gear_detail(request, gear_id):
    g = Gear.objects.get(id=gear_id)
    return render(request, 'gear/detail.html', {
        'g': g
    })

class GearCreate(CreateView):
    model = Gear
    fields = '__all__'

class GearUpdate(UpdateView):
    model = Gear
    fields = '__all__'

class GearDelete(DeleteView):
    model = Gear
    success_url = '/gear'