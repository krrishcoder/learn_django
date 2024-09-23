from django.urls import path
from . import views

#URL conNFIGURATION

urlpatterns = [
    path('hello/', views.say_hello) # passing reference to function
]