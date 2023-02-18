from django.db import models

class Services(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Изображение', upload_to='services', null=True, blank=True)
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Добавлено в', auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title}'

class ServicesInclude(models.Model):
    service = models.ForeignKey(to=Services, on_delete=models.CASCADE)
    denotation = models.CharField(max_length=255, verbose_name='Услуги')