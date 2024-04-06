from django.db import models
from django.urls import reverse


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
