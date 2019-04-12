from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, RichTextFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


class ArticlePage(Page):
   author = models.CharField(max_length=255)
   subtitle = models.CharField(max_length=150, null=True, blank=True)
   body = RichTextField()

   content_panels = Page.content_panels + [
   FieldPanel('author'),
   FieldPanel('subtitle'),
   RichTextFieldPanel('body')
]