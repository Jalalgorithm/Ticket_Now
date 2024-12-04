from django.urls import path
from . import views

urlpatterns=[
    # item list
    path('events/' ,views.EventListCreate.as_view(), name="event_list_create"),
    #event details
    path('events/<int:pk>/' , views.EventListCreate.as_view() ),
    
    #catgory detail
    path('category/<int:pk>/' , views.EventDetail.as_view() ), 
    
    #category list
    path('category/' , views.EventDetail.as_view() , name='event_detail' )
]