from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Coupon, Space, Customer, Branch, Room, Table, Desk

# Coupon views
def coupon_detail(request, coupon_id):
    coupon = get_object_or_404(Coupon, id=coupon_id)
    data = {
        'id': coupon.id,
        'space': coupon.space_id,
        'code': coupon.code,
        'discount_amount': coupon.discount_amount,
        'expiration_date': coupon.expiration_date,
        'is_expired': coupon.is_expired(),
    }
    return JsonResponse(data)

def all_coupons(request):
    coupons = Coupon.objects.all()
    data = [{'id': coupon.id, 'code': coupon.code} for coupon in coupons]
    return JsonResponse(data, safe=False)

# Space views
def space_detail(request, space_id):
    space = get_object_or_404(Space, id=space_id)
    data = {
        'id': space.id,
        'owner': space.owner_id,
        'name': space.name,
        'slogan': space.slogan,
        'space_address': space.space_adress,
    }
    return JsonResponse(data)

def all_spaces(request):
    spaces = Space.objects.all()
    data = [{'id': space.id, 'name': space.name, 'owner':space.owner_id,'slogan': space.slogan,} for space in spaces]
    return JsonResponse(data, safe=False)

# Customer  views



# Branch views


# Room views
# Table views
# Desk views
# Room views
# Room views
# Room views