from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import  PermissionsMixin



class UserManager(BaseUserManager):
    def create_user(self,email = None,first_name = None,last_name = '',password = None,*args, **kwargs):
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password id required")
        if not first_name:
            raise ValueError("Last Name is required")
        user = self.model(email = email ,last_name = last_name,first_name = first_name,**kwargs)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,last_name,first_name,password,**kwargs):
        kwargs.setdefault("is_staff",True)
        kwargs.setdefault("is_superuser",True)
        user = self.create_user(email = email,password=password,first_name=first_name,last_name=last_name,**kwargs)
        return user

class User(AbstractUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=340)
    last_name = models.CharField(max_length=340)
    username = models.CharField(unique=False,max_length=90)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = UserManager()
    

class RiderProfile(models.Model):
    
    state = models.CharField(max_length=200)
    lga = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    dob = models.DateField()
    phone = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='rider_profile')
    busy = models.BooleanField(default=False)
    total_star = models.IntegerField(default=0)
    pic = models.ImageField(upload_to='rider_pics/')

class CustomerProfile(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')


class Order(models.Model):
    pickup_location = models.TextField(default="")
    senders_phone_number = models.CharField(blank=True,max_length=90)
    delivery_location = models.TextField(default="")
    receivers_phone_number = models.CharField(blank=True,max_length=90)
    item_description = models.TextField(default="")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_rides')
    driver = models.ForeignKey(RiderProfile, on_delete=models.CASCADE, related_name='customer_rides',null = True,blank = True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    

    def __str__(self) -> str:
        return f'{self.customer.email} ordered on {self.date_ordered}'

    

class Prices(models.Model):
    name = models.CharField(max_length=120)
    descripton1 = models.TextField()
    price = models.IntegerField()
    descripton2 = models.TextField()
