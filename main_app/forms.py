from django.forms import ModelForm
from .models import Serviced

class ServicedForm(ModelForm):
    class Meta:
        model = Serviced
        fields = ['date', 'serviced']