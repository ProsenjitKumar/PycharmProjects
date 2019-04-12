from django.contrib import admin
from .models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['first_name', 'last_name', 'email', 'address', 'house_address']
    list_display = ['first_name', 'last_name', 'email', 'address', 'house_address']
    list_filter = ['first_name', 'last_name', 'email', 'address', 'house_address']


admin.site.register(UserAccount, UserAccountAdmin)