from django.db import models
from django_quill.fields import QuillField

# Create your models here.
class Project(models.Model):

    SECTOR_LIST = (
        ('Public','Public'),
        ('Private','Private'),
        ('Non-governmental','Non-governmental'),
        ('Local governance','Local governance'),
    )
    name_of_client = models.CharField(max_length=255, verbose_name='Имя клиента')
    financing_agency = models.CharField(max_length=255, verbose_name='Финансовое агентство')
    country = models.CharField(max_length=255, verbose_name='Страна')
    sector = models.CharField(max_length=255, choices=SECTOR_LIST, verbose_name='Сектор')
    month = models.CharField(verbose_name='Месяц', max_length=255)
    year = models.IntegerField(verbose_name='Год')
    projects_detail = QuillField()
    client = models.ForeignKey(to='clients.OurClients', on_delete=models.CASCADE, verbose_name='Клиент', null=True, blank=True)
    clients_logo = models.ImageField(upload_to='clients_logo', verbose_name='Логотип клиента', null=True, blank=True)
