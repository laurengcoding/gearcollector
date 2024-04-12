from django.contrib import admin

from .models import Gear, Serviced, Gig

admin.site.register(Gear)
admin.site.register(Serviced)
admin.site.register(Gig)