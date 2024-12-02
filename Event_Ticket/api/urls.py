from django.urls import path
from . import views

urlpatterns=[
    path('events/' ,views.EventListCreate.as_view({'get':'list'}), name="event-view-ticket")
]