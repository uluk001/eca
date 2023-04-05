from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Имя', null=True, blank=True)
    email = models.EmailField(verbose_name='Электронная почта', null=True, blank=True)
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', null=True, blank=True)


class Resume(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Электронная почта', null=True, blank=True)
    resume = models.FileField(upload_to='resume')
