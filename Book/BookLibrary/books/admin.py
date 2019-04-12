from django.contrib import admin
from .models import (
    Category,
    Author,
    Book,
    BookInstance,
)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'published', 'publisher']
    search_fields = ['title', 'isbn']


admin.site.register(Book, BookAdmin)


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'imprint', 'due_back']


admin.site.register(BookInstance, BookInstanceAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']


admin.site.register(Author, AuthorAdmin)