from django.urls import path
from .views import image_request  

app_name ='app'
urlpatterns =[
    path('',image_request,name='image_request'),
]