from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import *
from reservation.models import *
from space.models import *
# Create your views here.

#************************************************#
## Get All Reservations ## ListCreateAPIView
class ApiReservations(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


## Get Reservation Details ## RetrieveUpdateDestroyAPIView
class ApiReservation(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# @api_view(['GET','PUT','DELETE'])
# def api_reservation(request,pk):
#     reservation =  get_object_or_404(Reservation,pk=pk)
#     if request.method =="GET":
#         serializer = ReservationSerializer(reservation)
#         return Response(serializer.data)
#     if request.method =="PUT":
#         serializer = ReservationSerializer(reservation,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     if request.method =="DELETE":
#         reservation.delete()
#         return Response(status=HTTP_204_NO_CONTENT)
    

#************************************************#
## Get All Customer  ## ListCreateAPIView

class ApiCustomers(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

## Get Customer Details ## RetrieveUpdateDestroyAPIView

class ApiCustomer(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

#************************************************#
## Get All Spaces  ## 


class ApiSpaces(ListCreateAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer

## Get Space Details ##

class ApiSpace(RetrieveUpdateDestroyAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer

#************************************************#
## Get All Branchs  ##

class ApiBranchs(ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

## Get Branch Details ##

class ApiBranch(RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

#************************************************#
## Get All Rooms  ##

class ApiRooms(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

## Get Room Details ##

class ApiRoom(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

#************************************************#
## Get All Tables  ##

class ApiTables(ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

## Get Tables Details ##

class ApiTable(RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

#************************************************#
## Get All Desks  ##

class ApiDesks(ListCreateAPIView):
    queryset = Desk.objects.all()
    serializer_class = DeskSerializer

## Get Desk Details ##

class ApiDesk(RetrieveUpdateDestroyAPIView):
    queryset = Desk.objects.all()
    serializer_class = DeskSerializer

#************************************************#