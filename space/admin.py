# admin.py

from django.contrib import admin
from .models import Customer, Space, Branch, Room, Desk, Table
from reservation.models import *
# Register your models here.

admin.site.site_header =    "SPACY Administration Panel"
admin.site.site_title  =    "Welcome To The Admin Panel"
admin.site.index_title =    "SPACY Admin Panel"



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    # Your custom configuration for the Room model in the admin panel
    list_display    = ["user", "space_name", "first_name", "last_name", "phone_number", "email", "date_of_birth",]
    list_filter     = ["user", "space_name", "first_name", "last_name", "phone_number", "email", "date_of_birth",]
    search_fields   = ["user", "space_name", "first_name", "last_name", "phone_number", "email", "date_of_birth",]


@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    # Your custom configuration for the Room model in the admin panel
    list_display    = ["name", "owner", "slogan"]
    list_filter     = ["name", "owner" , "slogan"]
    search_fields   = ["name", "owner" , "slogan"]


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    # Your custom configuration for the Room model in the admin panel
    list_display    = ["name", "space"]
    list_filter     = ["name", "space" ]
    search_fields   = ["name", "space" ]

    
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    # Your custom configuration for the Room model in the admin panel
    list_display    = ["name", "room_cost" , "branch"]
    list_filter     = ["name", "room_cost" ]
    search_fields   = ["name", "room_cost" ]

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    # Your custom configuration for the Desk model in the admin panel
    list_display    = ["name", "table_cost" , "room"]
    list_filter     = ["name", "table_cost" ]
    search_fields   = ["name", "table_cost" ]

@admin.register(Desk)
class DeskAdmin(admin.ModelAdmin):
    # Your custom configuration for the Desk model in the admin panel
    list_display    = ["name", "desk_cost" , "room"]
    list_filter     = ["name", "desk_cost" ]
    search_fields   = ["name", "desk_cost" ]


# admin.site.register(Space)
# admin.site.register(Customer)
# admin.site.register(Branch)
# admin.site.register(Room)
# admin.site.register(Desk)
# admin.site.register(Table)
