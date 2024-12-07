from rest_framework import serializers
from .models import Event , EventCategory , TicketType


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields='__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=EventCategory
        fields='__all__' 
        

class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=TicketType
        fields='__all__'
    
    