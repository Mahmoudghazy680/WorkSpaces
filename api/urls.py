from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('reservations/', api_reservations),
    path('reservations/<int:pk>', api_reservation),
    
    path('customers/', api_customers),
    path('customers/<int:pk>', api_customer),
    
    path('spaces/', api_spaces),
    path('spaces/<int:pk>', api_space),
    
    path('branchs/', api_branchs),
    path('branchs/<int:pk>', api_branch),
    
    path('rooms/', api_rooms),
    path('rooms/<int:pk>', api_room),
    
    path('tables/', api_tables),
    path('tables/<int:pk>', api_table),
    
    path('desks/', api_desks),
    path('desks/<int:pk>', api_desk),
    
]