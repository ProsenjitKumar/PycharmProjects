from django.contrib import admin
from .models import Passenger


class PassenegerAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'ticket_class', 'survived']
    list_per_page = 10
    search_fields = ['name']

admin.site.register(Passenger, admin_class=PassenegerAdmin)
