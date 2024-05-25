from django.conf import settings
from django.db import models

# Create your models here.
from space.models import *
from datetime import datetime, timedelta, timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxLengthValidator
from django.utils import timezone

Shared='Shared'
Private='Private'
RoomStatus = (
                (Shared,'Shared'),
                (Private,'Private'),
        )

####################### Coupons #######################

class Coupon(models.Model):
    space = models.ForeignKey("space.space", default=None, on_delete=models.CASCADE, verbose_name = ("Space"),null=True, blank=True)
    code = models.CharField(max_length=20, unique=True)
    discount_amount = models.DecimalField(max_digits=5, decimal_places=2)
    expiration_date = models.DateTimeField()
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='coupons',null=True, blank=True,)
    
    def is_expired(self):
        return self.expiration_date < timezone.now()
        print ("Sorry, this Coupon is Expired.")

    def __str__(self):
        return f"{self.code}"
      
######################## Reservations #######################

class Reservation(models.Model):
    booking_id      = models.BigAutoField(primary_key=True)
    customer        = models.ForeignKey("space.Customer", verbose_name = ("Customer Name "), on_delete=models.CASCADE)
    customer_phone  = models.CharField(max_length=50, null=True, blank=True, verbose_name = ("Customer Phone "))
    customer_email  = models.EmailField(max_length=254,null=True, blank=True,  verbose_name = ("Customer E-mail "))
    check_in        = models.TimeField(null=True,default='00:00', blank=True, auto_now=False, auto_now_add=False, verbose_name = ("Check in "))
    check_out       = models.TimeField(null=True, default='00:00', blank=True, auto_now=False, auto_now_add=False, verbose_name = ("Check out "))
    status          = models.CharField(max_length=50, choices=RoomStatus, default=Shared)
    room_number     = models.ForeignKey("space.Room", null=True, blank=True,  on_delete=models.CASCADE, verbose_name = ("Room Number "))
    table_number    = models.ForeignKey("space.Table", null=True, blank=True,  on_delete=models.CASCADE, verbose_name = ("Table Number "))
    desk_number     = models.ForeignKey("space.Desk", null=True, blank=True,  on_delete=models.CASCADE, verbose_name = ("Desk Number "))
    price           = models.IntegerField(default=0, verbose_name= ("Cost "))
    discount        = models.IntegerField(default=0)
    coupon          = models.ForeignKey(Coupon, on_delete=models.CASCADE ,null=True, blank=True, verbose_name = ("Coupon"))
    want_reminder   = models.BooleanField(default=False, verbose_name="Want Reminder")
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    additional_info = models.TextField(null=True, blank=True , verbose_name = ("additional info  "), validators=[MaxLengthValidator(limit_value=500, 
                            message="Message is too long")])

    def __str__(self):
        return f"Our Client {self.customer} - was here " \
               f"{self.check_in.strftime('From :  %H:%M')} -  To : " \
               f"{self.check_out.strftime(' %H:%M')} - At :  "\
               f"{self.room_number} / {self.desk_number}"\
               f" -  Reservation Number :{self.booking_id}"
  
  
    @property
    def duration(self):
        # Calculate duration as a timedelta
        start_datetime = datetime.combine(datetime.today(), self.check_in)
        end_datetime = datetime.combine(datetime.today(), self.check_out)
        duration = end_datetime - start_datetime

        # Extract total hours from timedelta
        total_hours = duration.total_seconds() / 3600
        rounded_duration = round(total_hours, 1)

        # If you want to convert it to an integer if there are no decimal places
        rounded_duration = int(rounded_duration) if rounded_duration.is_integer() else rounded_duration
        return rounded_duration
 
    @property
    def total_price(self):
        # Calculate total price by multiplying duration in hours with the price per hour
        total = self.duration * self.price

        # Check for a discount
        if self.discount:
            total -= self.discount
        elif self.coupon:
            # Check if the coupon is not expired before applying the discount
            if self.coupon.expiration_date <= timezone.now():
                total -= self.coupon.discount_amount
            else:
                # Handle the case where the coupon is expired
                # (you may want to provide some feedback or take alternative actions)
                pass

        return total

        rounded_total = round(total, 1)
        # If you want to convert it to an integer if there are no decimal places
        # Check if rounded_total is an integer
        if isinstance(rounded_total, int):
            return int(rounded_total)
        else:
            return rounded_total

    class Meta:
        verbose_name        = _("Reservation")
        verbose_name_plural =  _('Reservation')

    def set_price_based_on_status(self):
            # Automatically set the price based on the chosen status
            if self.status == Shared and self.desk_number:
                self.price = self.desk_number.desk_cost
            elif self.status == Shared and self.table_number:
                self.price = self.table_number.table_cost
            elif self.status == Private and self.room_number:
                self.price = self.room_number.room_cost
            else:
                # Handle other room statuses if needed
                pass

    def save(self, *args, **kwargs):
        self.set_price_based_on_status()
        super().save(*args, **kwargs)

        # Handle reminder logic if want_reminder is True
        if self.want_reminder:
            # Placeholder for reminder logic
            # You may want to implement this using Celery or other asynchronous task handling
            # For now, print a message as a placeholder
            print(f"Reminder for Reservation {self.pk}: Send reminder to {self.customer.email} for check-in on {self.check_in}")
