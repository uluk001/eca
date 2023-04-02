from django.db import models
from django_quill.fields import QuillField


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория')

    def __str__(self) -> str:
        return f'{self.title}'


class OurClients(models.Model):
    сompany_name = models.CharField(max_length=255, verbose_name='Название компании')
    content = QuillField(verbose_name='Контент')
    image = models.ImageField(upload_to='clients', verbose_name='Изображение')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self) -> str:
        return f'{self.сompany_name}'
    

class PartnerImage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Компания')
    image = models.ImageField(upload_to='clients', verbose_name='Изображение')

    def __str__(self) -> str:
        return f'{self.title}'