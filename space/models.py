from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from reservation.models import Coupon
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

#################### space details ####################
        
class Space(models.Model):
    owner = models.ForeignKey("Customer", on_delete=models.CASCADE, verbose_name = ("Owner Name"),null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name = ("Space Name"))
    slogan = models.CharField(max_length=300, blank=True, null=True, verbose_name = ("Slogan"))
    space_adress = models.CharField(max_length=255, verbose_name = ("Adress"),null=True, blank=True)

    class Meta:
        verbose_name        = _("Space")
        verbose_name_plural = _('2.Spaces')
 
    def __str__(self):
        return self.name

#################### customer details ####################
# user=settings.AUTH_USER_MODEL

class Customer(models.Model):   
    space_name = models.ForeignKey(Space, on_delete=models.CASCADE, blank=True, null=True, verbose_name = ("Space"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = ("Customer"))
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True , on_delete=models.CASCADE, verbose_name = ("Customer"))
    # password = models.CharField(max_length=128, null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True, null=True, verbose_name = ("First Name"))
    last_name = models.CharField(max_length=30, blank=True, null=True, verbose_name = ("Last Name"))
    email = models.EmailField(blank=True, null=True, verbose_name = ("Email"))
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name = ("Phone Number"))
    address = models.TextField(blank=True, null=True, verbose_name = ("Adress "))
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True, verbose_name = ("Profile Photo"))
    applied_coupons = models.ManyToManyField('reservation.Coupon', blank=True, verbose_name = ("Applied coupons"))
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)
    def __str__(self):
        # return f"{self.user}"
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _('1.Customers')

####################  Braches details ####################
    
class Branch(models.Model):
    space = models.ForeignKey(Space, on_delete=models.CASCADE, verbose_name = ("Space"))
    name = models.CharField(max_length=255, verbose_name = ("Branch Name"))
    branch_adress = models.CharField(max_length=255, verbose_name = ("Adress"),null=True, blank=True)


    class Meta:
        verbose_name        = _("Branch")
        verbose_name_plural = _('3.Branchs')
 
    def __str__(self):
        return self.name
    
#################### Rooms details ####################
    
class Room(models.Model):
    branch      = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name = ("Branch Name"))
    name        = models.CharField(max_length=255, verbose_name = ("Room Name"))
    room_cost   = models.DecimalField(default= 50,max_digits=5, decimal_places=2, verbose_name = ("Room Cost/H "))

    class Meta:
        verbose_name        = _("Room")
        verbose_name_plural = _('4.Rooms')
 
    def __str__(self):
        return self.name
    
#################### Tables details ####################
    
class Table(models.Model):
    room        = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name = ("Room Name"))
    name        = models.CharField(max_length=255, verbose_name = ("Table Name"))
    table_cost   = models.DecimalField(default= 50,max_digits=5, decimal_places=2, verbose_name = ("Table Cost/H "))
    class Meta:
        verbose_name        = _("Table")
        verbose_name_plural = _('5.Tables')
 
    def __str__(self):
        return self.name
    
####################  Desks details ####################
class Desk(models.Model):
    room        = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name = ("Room Name"))
    name        = models.CharField(max_length=255, verbose_name = ("Desk Name"))
    desk_cost   = models.DecimalField(default= 50,max_digits=5, decimal_places=2, verbose_name = ("Desk Cost/H "))

    class Meta:
        verbose_name        = _("Desk")
        verbose_name_plural = _('6.Desks')
 
    def __str__(self):
        return self.name
    
    
def update_last_login(sender, user, **kwargs):
    """
    A signal receiver which updates the last_login date for
    the user logging in.
    """
    user.last_login = timezone.now()
    user.save(update_fields=["last_login"])

