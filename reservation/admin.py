from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Reservation, Coupon


@admin.register(Reservation)
class BookingAdmin(admin.ModelAdmin):
    # Your custom configuration for the Desk model in the admin panel
    list_display = ('booking_id','customer', 'check_in', 'check_out',"duration", 'status', 'room_number', 'table_number' , 
                    'desk_number', 'price', 'discount','coupon', 'total_price')
    list_display_links = ('booking_id','customer', 'check_in', 'check_out',"duration", 'status', 'room_number', 'table_number' , 
                    'desk_number', 'price', 'discount','coupon', 'total_price')
    list_filter = ('customer', 'status', 'room_number', 'desk_number', 'price', 'discount', 'want_reminder')
    # autocomplete_fields = ["user__first_name", 'user__email', 'user__last_name']
    readonly_fields = ("created_at" , "updated_at" )
    search_fields = ('room__name', 'table__room_number', 'desk__desk_number')
    

@admin.register(Coupon)
class Coupondmin(admin.ModelAdmin):
    # Your custom configuration for the Desk model in the admin panel
    list_display    = ('code','discount_amount', 'expiration_date')
    list_filter     = ('code', 'expiration_date' )
    search_fields   = ('code','discount_amount', 'expiration_date')
    list_display_links = ('code','discount_amount', 'expiration_date')

# admin.site.register(Calendar)
# admin.site.register(Coupon)