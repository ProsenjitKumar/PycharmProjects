from django.contrib import admin
from .models import Post, Author, Category, Tag

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Category)