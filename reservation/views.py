from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Reservation


def all_reservations(request):
    # Retrieve all reservations from the database
    reservations = Reservation.objects.all()
    
    # Serialize the reservations to JSON
    data = []
    for reservation in reservations:
        reservation_data = {
            'booking_id': reservation.booking_id,
            'space': reservation.space_id,
            'branch': reservation.branch_id,
            'customer': reservation.customer_id,
            'customer_phone': reservation.customer_phone,
            'customer_email': reservation.customer_email,
            'check_in': reservation.check_in,
            'check_out': reservation.check_out,
            'status': reservation.status,
            'room_number': reservation.room_number_id,
            'table_number': reservation.table_number_id,
            'desk_number': reservation.desk_number_id,
            'price': reservation.price,
            'discount': reservation.discount,
            'coupon': reservation.coupon_id,
            'want_reminder': reservation.want_reminder,
            'created_at': reservation.created_at,
            'updated_at': reservation.updated_at,
            'additional_info': reservation.additional_info,
        }
        data.append(reservation_data)
    
    # Return the reservations data as JSON response
    return JsonResponse(data, safe=False)


def reservation_detail(request, booking_id):
    # Retrieve the reservation object from the database
    reservation = get_object_or_404(Reservation, booking_id=booking_id)
    # Serialize the reservation object to JSON
    data = {
        'booking_id': reservation.booking_id,
        'space': reservation.space_id,
        'branch': reservation.branch_id,
        'customer': reservation.customer_id,
        'customer_phone': reservation.customer_phone,
        'customer_email': reservation.customer_email,
        'check_in': reservation.check_in,
        'check_out': reservation.check_out,
        'status': reservation.status,
        'room_number': reservation.room_number_id,
        'table_number': reservation.table_number_id,
        'desk_number': reservation.desk_number_id,
        'price': reservation.price,
        'discount': reservation.discount,
        'coupon': reservation.coupon_id,
        'want_reminder': reservation.want_reminder,
        'created_at': reservation.created_at,
        'updated_at': reservation.updated_at,
        'additional_info': reservation.additional_info,
    }
    # Return the reservation data as JSON response
    return JsonResponse(data)

