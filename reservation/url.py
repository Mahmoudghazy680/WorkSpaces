from django.urls import path
from .views import reservation_detail, all_reservations
from reservation import views

urlpatterns = [
    # reservation URL
    path('reservation/<int:booking_id>/', views.reservation_detail, name='reservation-detail'),
    path('reservations/', all_reservations, name='all-reservations'),
]