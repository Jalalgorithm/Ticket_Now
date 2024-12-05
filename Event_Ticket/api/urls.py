from django.urls import path
from . import views

urlpatterns=[
    # item list
    path('events/' ,views.EventListCreate.as_view(), name="event_list_create"),
    #event details
    path('events/<int:pk>/' , views.EventDetail.as_view() , name='event_detail' ),
    
    #catgory detail
    path('category/<int:pk>/' , views.EventCategoryDetail.as_view() , name='event_category_detail' ), 
    
    #category list
    path('category/' , views.CategoryListCreate.as_view() , name='category_list_create' )
]