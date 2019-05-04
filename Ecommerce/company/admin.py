from django.contrib import admin
from .models import ClientCompany


# Register your models here.
class ClientCompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'place']
    list_per_page = 10


admin.site.register(ClientCompany, ClientCompanyAdmin)
