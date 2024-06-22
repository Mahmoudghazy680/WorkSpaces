from django.urls import path, include
from .views import *
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register('reservations', ReservationViewsets)
router.register('customers', CustomerViewsets)
router.register('spaces', SpaceViewsets)
router.register('branchs', BranchViewsets)
router.register('rooms', RoomViewsets)
router.register('tables', TableViewsets)
router.register('desks', DeskViewsets)
router.register('copuon', CopunViewsets)

# urlpatterns = router.urls
urlpatterns = [
    path('',include(router.urls)),

    # API Class Based View
    path('reservations/', ApiReservations.as_view()),
    path('reservations/<int:pk>', ApiReservation.as_view()),
        
    path('customers/', ApiCustomers.as_view()),
    path('customers/<int:pk>', ApiCustomer.as_view()),
 
    path('spaces/', ApiSpaces.as_view()),
    path('spaces/<int:pk>', ApiSpace.as_view()),
 
    path('branchs/', ApiBranchs.as_view()),
    path('branchs/<int:pk>', ApiBranch.as_view()),
 
    path('rooms/', ApiRooms.as_view()),
    path('rooms/<int:pk>', ApiRoom.as_view()),
 
    path('tables/', ApiTables.as_view()),
    path('tables/<int:pk>', ApiTable.as_view()),
 
    path('desks/', ApiDesks.as_view()),
    path('desks/<int:pk>', ApiDesk.as_view()),
  
    path('copuon/', ApiCoupons.as_view()),



    # path('api-token-auth/', views.obtain_auth_token),

]