from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from reservation.models import *
from space.models import *
# Create your views here.


## Get All Reservations ##
@api_view(['GET'])
def api_reservations(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)

## Get Reservation Details ##
@api_view(['GET'])
def api_reservation(request,pk):
    reservation =  get_object_or_404(Reservation,pk=pk)
    serializer = ReservationSerializer(reservation)
    return Response(serializer.data)

#************************************************#

## Get All Customers  ##
@api_view(['GET'])
def api_customers(request):
    customers =  Customer.objects.all()
    serializer = CustomerSerializer(customers,many=True)
    return Response(serializer.data)

## Get Customer Details ##
@api_view(['GET'])
def api_customer(request,pk):
    customer =  get_object_or_404(Customer,pk=pk)
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)

#************************************************#

## Get All Spaces  ##
@api_view(['GET'])
def api_spaces(request):
    spaces =  Space.objects.all()
    serializer = SpaceSerializer(spaces,many=True)
    return Response(serializer.data)

## Get Space Details ##
@api_view(['GET'])
def api_space(request,pk):
    space =  get_object_or_404(Space,pk=pk)
    serializer = SpaceSerializer(space)
    return Response(serializer.data)

#************************************************#

## Get All Branchs  ##
@api_view(['GET'])
def api_branchs(request):
    branch =  Branch.objects.all()
    serializer = BranchSerializer(branch,many=True)
    return Response(serializer.data)

## Get Branch Details ##
@api_view(['GET'])
def api_branch(request,pk):
    branch =  get_object_or_404(Branch,pk=pk)
    serializer = BranchSerializer(branch)
    return Response(serializer.data)

#************************************************#

## Get All Rooms  ##
@api_view(['GET'])
def api_rooms(request):
    room =  Room.objects.all()
    serializer = RoomSerializer(room,many=True)
    return Response(serializer.data)

## Get Room Details ##
@api_view(['GET'])
def api_room(request,pk):
    room =  get_object_or_404(Room,pk=pk)
    serializer = RoomSerializer(room)
    return Response(serializer.data)

#************************************************#

## Get All Tables  ##
@api_view(['GET'])
def api_tables(request):
    table =  Table.objects.all()
    serializer = TableSerializer(table,many=True)
    return Response(serializer.data)

## Get Tables Details ##
@api_view(['GET'])
def api_table(request,pk):
    table =  get_object_or_404(Table,pk=pk)
    serializer = TableSerializer(table)
    return Response(serializer.data)

#************************************************#

## Get All Desks  ##
@api_view(['GET'])
def api_desks(request):
    desk =  Desk.objects.all()
    serializer = DeskSerializer(desk,many=True)
    return Response(serializer.data)

## Get Desk Details ##
@api_view(['GET'])
def api_desk(request,pk):
    desk =  get_object_or_404(Desk,pk=pk)
    serializer = DeskSerializer(desk)
    return Response(serializer.data)

#************************************************#