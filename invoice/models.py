from django.conf import settings
from django.db import models

# Create your models here.


class UserCheckout(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    email = models.EmailField(unique=True)


    def __unicode__(self):
        return self.email


ADDRESS_TYPE = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping'),
)


class UserAddress(models.Model):
    user = models.ForeignKey(UserCheckout)
    type = models.CharField(max_length=120, choices=ADDRESS_TYPE)
    street = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=10)

    def __unicode__(self):
        return self.street

# class Order(models.Model):
    #usercheckout
