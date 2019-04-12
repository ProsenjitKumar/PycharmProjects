from django.conf.urls import re_path
from .views import (
    HomeView,
    ticket_class_view,
    ticket_class_view_2,
    ticket_class_view_3,
    json_example,
    chart_data,
)

urlpatterns = [
    re_path('^$', HomeView.as_view(), name='home'),
    re_path('ticket-class-view/', ticket_class_view, name='ticket-class-view'),
    re_path('ticket-class-view-2/', ticket_class_view_2,             name='ticket_class_view_2'),
    re_path('ticket-class-view-3/', ticket_class_view_3, name='ticket_class_view_3'),
    re_path('json-example/', json_example, name='json_example'),
    re_path('json-example/data/', chart_data, name='chart_data'),
]
