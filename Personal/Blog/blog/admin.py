from django.contrib import admin
from .models import (
    Post,
    PostManager,
    Profile,
    Lesson
)

#admin.site.register(PostManager)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Lesson)