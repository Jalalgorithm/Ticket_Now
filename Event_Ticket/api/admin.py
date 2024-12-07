from django.contrib import admin
from .models import Event , EventCategory , TicketType


admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(TicketType)
# Register your models here.
