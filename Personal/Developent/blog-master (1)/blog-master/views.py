from django.views.generic import TemplateView


class BlogIndexView(TemplateView):
    template_name = 'blog/index.html'
