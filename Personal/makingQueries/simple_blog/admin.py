from django.contrib import admin
from .models import (
    Blog,
    Author,
    Entry
)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'tagline',]
    list_per_page = 10

admin.site.register(Blog, BlogAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email',]
    list_per_page = 10

admin.site.register(Author, AuthorAdmin)

class EntryAdmin(admin.ModelAdmin):
    list_display = ['blog', 'headline', 'pub_date', 'mod_date',
                    'n_comments', 'n_pingbacks', 'rating']
    list_per_page = 10

admin.site.register(Entry, EntryAdmin)
