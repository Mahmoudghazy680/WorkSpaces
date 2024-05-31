from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('reservations/', api_reservations),
    path('reservations/<int:pk>', api_reservation),
    
]