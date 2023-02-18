from django.db import models

# Create your models here.
class Project(models.Model):
    MONTH_LIST = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    )
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
    month = models.CharField(choices=MONTH_LIST, verbose_name='Месяц', max_length=255)
    year = models.IntegerField(verbose_name='Год')
    projects_detail = models.TextField(max_length=255, verbose_name='Детали проекта')