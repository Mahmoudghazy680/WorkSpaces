from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from reservation.models import *
from space.models import *
# Create your views here.


## Get All Reservations ##
@api_view()
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
