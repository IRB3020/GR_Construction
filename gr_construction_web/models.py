from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
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
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ManagerManager(models.Manager):
    def get_by_natural_key(self, username):
        return self.get(user__username=username)
    