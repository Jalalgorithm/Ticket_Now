from django.shortcuts import render
from rest_framework import generics
from .models import Event , EventCategory
from .serializers import EventSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class EventListCreate (generics.ListCreateAPIView):
    serializer_class = EventSerializer
    
    def get_queryset(self):
        queryset = Event.objects.all()
        event_category = self.request.query_params.get('category')
        if event_category is not None:
            queryset = queryset.filter(category=event_category) 
        return queryset
    
    
class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    