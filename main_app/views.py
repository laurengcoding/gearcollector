from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Gear, Gig

from .forms import ServicedForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def gear_index(request):
    gear = Gear.objects.filter(user=request.user)
    return render(request, 'gear/index.html', {
        'gear': gear
    })

@login_required
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

@login_required
def add_service(request, gear_id):
    serviced_form = ServicedForm(request.POST)
    if serviced_form.is_valid():
        new_service = serviced_form.save(commit=False)
        new_service.g_id = gear_id
        new_service.save()
    return redirect('detail', gear_id=gear_id)
    
@login_required
def add_gig(request, gear_id, gig_id):
    Gear.objects.get(id=gear_id).gigs.add(gig_id)
    return redirect('detail', gear_id=gear_id)

@login_required
def remove_gig(request, gear_id, gig_id):
    Gear.objects.get(id=gear_id).gigs.remove(gig_id)
    return redirect('detail', gear_id=gear_id)

class GearCreate(CreateView, LoginRequiredMixin):
    model = Gear
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GearUpdate(UpdateView, LoginRequiredMixin):
    model = Gear
    fields = '__all__'

class GearDelete(DeleteView, LoginRequiredMixin):
    model = Gear
    success_url = '/gear/'

# Gig CRUD ########################
    
class GigList(ListView, LoginRequiredMixin):
    model = Gig

class GigDetail(DetailView, LoginRequiredMixin):
    model = Gig

class GigCreate(CreateView, LoginRequiredMixin):
    model = Gig
    fields = '__all__'

class GigUpdate(UpdateView, LoginRequiredMixin):
    model = Gig
    fields = '__all__'

class GigDelete(DeleteView, LoginRequiredMixin):
    model = Gig
    success_url = '/gigs/'

# User Sign Up ######################
    
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup/html', context)