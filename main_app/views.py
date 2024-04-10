from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Gear, Gig

from .forms import ServicedForm

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
    serviced_form = ServicedForm()
    current_gig_ids = g.gigs.all().values_list('id')
    available_gigs = Gig.objects.exclude(id__in=current_gig_ids)
    return render(request, 'gear/detail.html', {
        'g': g,
        'serviced_form': serviced_form,
        'available_gigs': available_gigs
    })

def add_service(request, gear_id):
    serviced_form = ServicedForm(request.POST)
    if serviced_form.is_valid():
        new_service = serviced_form.save(commit=False)
        new_service.g_id = gear_id
        new_service.save()
    return redirect('detail', gear_id=gear_id)
    
def add_gig(request, gear_id, gig_id):
    Gear.objects.get(id=gear_id).gigs.add(gig_id)
    return redirect('detail', gear_id=gear_id)

def remove_gig(request, gear_id, gig_id):
    Gear.objects.get(id=gear_id).gigs.remove(gig_id)
    return redirect('detail', gear_id=gear_id)

class GearCreate(CreateView):
    model = Gear
    fields = '__all__'

class GearUpdate(UpdateView):
    model = Gear
    fields = '__all__'

class GearDelete(DeleteView):
    model = Gear
    success_url = '/gear/'

# Gig CRUD ########################
    
class GigList(ListView):
    model = Gig

class GigDetail(DetailView):
    model = Gig

class GigCreate(CreateView):
    model = Gig
    fields = '__all__'

class GigUpdate(UpdateView):
    model = Gig
    fields = '__all__'

class GigDelete(DeleteView):
    model = Gig
    success_url = '/gigs/'