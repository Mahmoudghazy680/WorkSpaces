from rest_framework import serializers
from reservation.models import *
from space.models import *

#*********************Reservation***************************#
class ReservationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Reservation model.

    This serializer serializes reservation data including booking ID, space,
    branch, customer details, check-in/out times, status, room/table/desk
    numbers, pricing, discounts, and timestamps.
    """
     
    class Meta:
        model = Reservation
        # fields = ['pk', 'space', 'branch', 'customer', 'price', 'created_at',  ]
        fields = ['pk','booking_id', 'space', 'branch', 'customer','customer_email', 'customer_phone', 'check_in', 'check_out', 'status', 'room_number', 'table_number', 'desk_number', 'price', 'discount', 'coupon', 'created_at', 'updated_at', ]

#*********************Space***************************#
class SpaceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Sapce model.
    This serializer serializes Space data including name, owner , slogan and space adress.
    """
     
    class Meta :
        model = Space
        fields = ['name','owner','slogan', 'space_adress',]

#*********************Customer***************************#
class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Customer model.

    This serializer serializes Customer data including user, related space, 
    first/last name, email, phone, address, birth date, gender, picture, 
    applied coupons, and last login for this customer.
    """
    
    class Meta :
        model = Customer
        fields = ['space_name', 'user', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'date_of_birth', 'gender', 'profile_picture', 'applied_coupons', 'last_login', ]

#**********************Branch**************************#
class BranchSerializer(serializers.ModelSerializer):
    """
    Serializer for the Branch model.
    This serializer serializes Branch data including 
    branch name, related space , and Branch adress.
    """
    class Meta :
        model = Branch
        fields = ['space','name','branch_adress', ]

#*********************Room***************************#
class RoomSerializer(serializers.ModelSerializer):
    class Meta :
        model = Room
        fields = ('space','branch','name', 'room_cost', )

#*********************Table***************************#
class TableSerializer(serializers.ModelSerializer):
    class Meta :
        model = Table
        fields = ('space','branch','room', 'name', 'table_cost')

#**********************Desk**************************#
class DeskSerializer(serializers.ModelSerializer):
    class Meta :
        model = Desk
        fields = ('space','branch','room', 'name', 'desk_cost')

#**********************Coupon**************************#
class CouponSerializer(serializers.ModelSerializer):
    class Meta :
        model = Coupon
        fields = ('space','code','discount_amount', 'expiration_date', 'users')

#************************************************#



