from django.db import models
from django_quill.fields import QuillField


class Members(models.Model):
    description = QuillField(verbose_name='Описание')
    image = models.ImageField(upload_to='associated_aca_memebers', verbose_name='Изображение')

class EcasRole(models.Model):
    member = models.ForeignKey(to=Members, on_delete=models.CASCADE, related_name='ecas_roles')
    title = QuillField(verbose_name='As eca expert was envoled', null=True, blank=True)
