from django.contrib import admin
from .models import Passenger

class PassengerAdmin(admin.ModelAdmin):
    list_display = ['name', 'sex', 'age', 'ticket_class']
    populated_fields = {'slug':('name',)}

admin.site.register(Passenger, PassengerAdmin)
