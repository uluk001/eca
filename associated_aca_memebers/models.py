from django.db import models
from django_quill.fields import QuillField


class Members(models.Model):
    description = QuillField(verbose_name='Описание')
    image = models.ImageField(upload_to='associated_aca_memebers', verbose_name='Изображение')
    ecas_role = QuillField(verbose_name='As eca expert was envoled', null=True, blank=True)
