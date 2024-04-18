from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.utils.translation import gettext as _


# Create your models here.
class WorkSite(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True, blank=True)
    bills = models.ManyToManyField('Bill', blank=True)
    final_shot = models.ImageField(upload_to='worksites/finished', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('worksite-detail', args=[str(self.id)])

    def google_maps_url(self):
        # Generate Google Maps URL based on the address
        return f"https://www.google.com/maps/search/?api=1&query={self.address}"


class Bill(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(_("Date"), default=date.today)

    def __str__(self):
        return f"${self.amount}"


class Client(models.Model):
    STATUS = (
        ('Active', 'First-Time Customer'),
        ('Active', 'Returning Customer'),
        ('Finished', 'Business Finished'),
        ('Finished', 'Business Pulled')
    )

    name = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS, blank=False)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])


class Manager(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ManagerManager(models.Manager):
    def get_by_natural_key(self, username):
        return self.get(user__username=username)
    