from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(verbose_name='Электронная почта')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
