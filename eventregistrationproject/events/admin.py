from django.contrib import admin
from .models import Events, Registrations

# Register your models here.
admin.site.register(Events)
admin.site.register(Registrations)