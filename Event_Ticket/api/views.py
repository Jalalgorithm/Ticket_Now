from django.shortcuts import render
from rest_framework import generics
from .models import Event , EventCategory , TicketType
from .serializers import EventSerializer , CategorySerializer ,TicketTypeSerializer
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
    

class EventCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = EventCategory.objects.all()
    

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = EventCategory.objects.all()
    serializer_class = CategorySerializer
    
class TicketTypeListCreate(generics.ListCreateAPIView):
    queryset = TicketType.objects.all()
    serializer_class = TicketTypeSerializer
    
    