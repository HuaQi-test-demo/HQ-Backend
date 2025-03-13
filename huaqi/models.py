from contextlib import nullcontext

from django.db import models

# Create your models here.
class userInfo(models.Model):
    name = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100,default='尊贵的用户')
    email = models.EmailField()
    password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100)

class earth_rate(models.Model):
    date_time = models.DateField()
    country = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    currency_sign = models.CharField(max_length=100)
    currency1_name = models.CharField(max_length=100)
    currency_rate1 = models.DecimalField(max_digits=10, decimal_places=6)
    currency2_name = models.CharField(max_length=100)
    currency_rate2 = models.DecimalField(max_digits=10, decimal_places=6)
    currency3_name = models.CharField(max_length=100)
    currency_rate3 = models.DecimalField(max_digits=10, decimal_places=6)
    currency4_name = models.CharField(max_length=100)
    currency_rate4 = models.DecimalField(max_digits=10, decimal_places=6)
    currency5_name = models.CharField(max_length=100)
    currency_rate5 = models.DecimalField(max_digits=10, decimal_places=6)
    currency6_name = models.CharField(max_length=100)
    currency_rate6 = models.DecimalField(max_digits=10, decimal_places=6)
    currency7_name = models.CharField(max_length=100)
    currency_rate7 = models.DecimalField(max_digits=10, decimal_places=6)
    currency8_name = models.CharField(max_length=100)
    currency_rate8 = models.DecimalField(max_digits=10, decimal_places=6)
    currency9_name = models.CharField(max_length=100, null=True, blank=True)
    currency_rate9 = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)

class country_currency(models.Model):
    country = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)

class date_currency_rate(models.Model):
    date = models.CharField(max_length=100)
    currency_1 = models.CharField(max_length=100)
    currency_2 = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=6)