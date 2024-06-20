from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from reservation.models import *
from space.models import *
from .filter import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter , OrderingFilter
# Create your views here.

#************************************************#
##| Get All Reservations ##| ListCreateAPIView
#************************************************#

class ApiReservations(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ReservationFilter
    search_fields = ['customer', 'customer_phone', 'room_number','table_number', 'desk_number']
    ordering_fields = ['booking_id','price','room_number',]
##| Get Reservation Details ##| RetrieveUpdateDestroyAPIView

class ApiReservation(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ReservationFilter
    search_fields = ['customer', 'customer_phone', 'room_number','table_number', 'desk_number']
    ordering_fields = ['booking_id','price',]


#************************************************#
##| Get All Customer  |## ListCreateAPIView
#************************************************#
class ApiCustomers(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CustomerFilter
    search_fields = ['user', 'customer_phone', 'first_name','last_name', 'email', 'gender']
    ordering_fields = ['user',]

##| Get Customer Details ##| RetrieveUpdateDestroyAPIView

class ApiCustomer(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

#************************************************#
##| Get All Spaces  |## 
#************************************************#

class ApiSpaces(ListCreateAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer

##| Get Space Details |##

class ApiSpace(RetrieveUpdateDestroyAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer

#************************************************#
#  ##| Get All Branchs  |##
#************************************************#

class ApiBranchs(ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

##| Get Branch Details |##

class ApiBranch(RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

#************************************************#
#  Get All Rooms  |##
#************************************************#

class ApiRooms(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

##| Get Room Details |##

class ApiRoom(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

#************************************************#
# ##| Get All Tables  |##
#************************************************#

class ApiTables(ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

##| Get Tables Details |##

class ApiTable(RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

#************************************************#
##| Get All Desks  |##
#************************************************#

class ApiDesks(ListCreateAPIView):
    queryset = Desk.objects.all()
    serializer_class = DeskSerializer

##| Get Desk Details |##

class ApiDesk(RetrieveUpdateDestroyAPIView):
    queryset = Desk.objects.all()
    serializer_class = DeskSerializer

#************************************************#
##|| Get All Coupons  |##
#************************************************#

class ApiCoupons(ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
