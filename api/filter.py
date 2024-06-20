from django_filters.rest_framework import FilterSet
from space.models import *
from reservation.models import *


class ReservationFilter (FilterSet): 
    class Meta:
        model = Reservation
        fields = {
            'booking_id'    :['exact'],
            'customer'      :['exact'],
            'customer_phone':['exact'],
            'status'        :['exact'],
            'room_number'   :['exact'],
            'table_number'  :['exact'],
            'desk_number'   :['exact'],
            'price'         :['gt','lt'],
            'coupon'        :['exact'],
            'created_at'    :['contains'],
        }

class CustomerFilter (FilterSet): 
    class Meta:
        model = Customer
        fields = {
            'user'          :['exact'],
            'first_name'    :['contains'],
            'last_name'     :['contains'],
            'email'         :['exact'],
            'phone_number'  :['exact'],
            'gender'        :['exact'],
        }


class SpaceFilter (FilterSet): 
    class Meta:
        model = Space
        fields = {
            'owner'    :['exact'],
            'name'     :['exact'],
            'slogan'   :['contains'],
            'space_adress'     :['contains'],
   
        }