from statistics import mode
from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    message = models.TextField(max_length = 255)