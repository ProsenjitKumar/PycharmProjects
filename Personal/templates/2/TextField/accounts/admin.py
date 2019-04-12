from django.contrib import admin
from .models import ArticlePage


class ArticlePageAdmin(admin.ModelAdmin):
    list_display = ['author', 'subtitle', 'body']


admin.site.register(ArticlePage, ArticlePageAdmin)
