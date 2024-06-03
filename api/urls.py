from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    # API Class Based View
    path('reservations/', ApiReservations.as_view()),
    path('reservations/<int:pk>', ApiReservation.as_view()),
        
    path('customers/', ApiCustomers.as_view()),
    path('customers/<int:pk>', ApiCustomer.as_view()),
 
    path('Spaces/', ApiSpaces.as_view()),
    path('Spaces/<int:pk>', ApiSpace.as_view()),
 
    path('branchs/', ApiBranchs.as_view()),
    path('branchs/<int:pk>', ApiBranch.as_view()),
 
    path('rooms/', ApiRooms.as_view()),
    path('rooms/<int:pk>', ApiRoom.as_view()),
 
    path('tables/', ApiTables.as_view()),
    path('tables/<int:pk>', ApiTable.as_view()),
 
    path('desks/', ApiDesks.as_view()),
    path('desks/<int:pk>', ApiDesk.as_view()),
  
       # API FBV  
    # path('reservations/',api_reservations), 
    # path('reservations/<int:pk>', api_reservation),
]