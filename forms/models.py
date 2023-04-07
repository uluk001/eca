from django.db import models
from django.core.mail import send_mail
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage


# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Имя', null=True, blank=True)
    email = models.EmailField(verbose_name='Электронная почта', null=True, blank=True)
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', null=True, blank=True)
    message = models.TextField(verbose_name='Сообщение')

    def send_message(self):
        full_name = self.full_name
        message = self.message
        email = self.email
        phone_number = self.phone_number

        send_mail(
            f'Сообщение от в {full_name}',
            f'''Вам пришло сообщение от администрации сайта eca.kg
От: {full_name}
            
Почта: {email}

Номер телефона: {phone_number}

{message}''',
            'eca.kg.adm@gmail.com',
            ['ulukmanmuratov@gmail.com'],
            fail_silently=False,
        )


class Resume(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Электронная почта', null=True, blank=True)
    resume = models.FileField(upload_to='resume')




@receiver(post_save, sender=Resume)  # CV sender to email
def send_resume(sender, instance, **kwargs):
    email = EmailMessage(
        'Новое резюме',
        f'Имя: {instance.first_name}\nФамилия: {instance.last_name}\nEmail: {instance.email}',
        'eca.kg.adm@gmail.com',
        ['ulukmanmuratov@gmail.com'],
    )
    email.attach_file(instance.resume.path)
    email.send()