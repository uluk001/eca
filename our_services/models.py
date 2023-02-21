from django.db import models
from django_quill.fields import QuillField

class Services(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Изображение', upload_to='services', null=True, blank=True)
    description = QuillField()
    created_at = models.DateTimeField(verbose_name='Добавлено в', auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title}'

class ServicesInclude(models.Model):
    service = models.ForeignKey(to=Services, on_delete=models.CASCADE)
    denotation = models.CharField(max_length=255, verbose_name='Услуги')