from django.db import models

# Create your models here.


class EventCategory(models.Model):
    name= models.CharField(max_length=100 , unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    

class Event(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    location=models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    category= models.ForeignKey(EventCategory , on_delete=models.CASCADE , related_name='events')
    
    def __str__(self):
        return self.title
    

    
    
    
    

