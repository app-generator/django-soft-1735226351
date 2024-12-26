# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    id_product = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    price_buy = models.IntegerField(null=True, blank=True)
    price_sell = models.IntegerField(null=True, blank=True)
    supplier = models.ForeignKey(supplier, on_delete=models.CASCADE)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Supplier(models.Model):

    #__Supplier_FIELDS__
    id_supplier = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Supplier_FIELDS__END

    class Meta:
        verbose_name        = _("Supplier")
        verbose_name_plural = _("Supplier")


class Product_Obs(models.Model):

    #__Product_Obs_FIELDS__
    id_product_obs = models.IntegerField(null=True, blank=True)
    id_product = models.ForeignKey(product, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Product_Obs_FIELDS__END

    class Meta:
        verbose_name        = _("Product_Obs")
        verbose_name_plural = _("Product_Obs")



#__MODELS__END
