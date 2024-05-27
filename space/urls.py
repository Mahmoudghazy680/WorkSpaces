from django.urls import path
from . import views

urlpatterns = [
    # Coupon URLs
    path('coupon/<int:coupon_id>/', views.coupon_detail, name='coupon-detail'),
    path('coupons/', views.all_coupons, name='all-coupons'),
    # Space URLs
    path('space/<int:space_id>/', views.space_detail, name='space-detail'),
    path('spaces/', views.all_spaces, name='all-spaces'),
]