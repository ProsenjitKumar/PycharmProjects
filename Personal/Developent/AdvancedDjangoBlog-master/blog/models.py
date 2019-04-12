from django.db import models
from django.utils import timezone
import datetime

class Author(models.Model):

    name = models.CharField(max_length=50, default=0)
    email = models.EmailField(unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    cat_name = models.CharField('category Name',max_length=50, default=0)
    cat_description = models.CharField('category Description',max_length=255, default=0)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.cat_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=50, default=0)
    tag_description = models.CharField(max_length=255, default=0)

    def __str__(self):
        return self.tag_name

class Post(models.Model):

    title = models.CharField(max_length=200, default=0)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    author = models.ForeignKey(Author)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title