from django.shortcuts import render
from rest_framework import generics
from .models import Event
from .serializers import EventSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class EventListCreate (generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    

