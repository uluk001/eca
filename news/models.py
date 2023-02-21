from django.db import models
from django_quill.fields import QuillField

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=775, verbose_name='Заголовок')
    content = QuillField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано в:')
    main_image = models.ImageField(upload_to='news/main_image', verbose_name='Изображение')

    def __str__(self):
        return f'{self.title}'

class NewImages(models.Model):
    news = models.ForeignKey(to=News, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news', verbose_name='Изображение')