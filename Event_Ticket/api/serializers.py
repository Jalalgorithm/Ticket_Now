from rest_framework import serializers
from .models import Event , EventCategory


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields='__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    model=EventCategory
    fields='__all__'