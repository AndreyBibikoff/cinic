from django.db import models


class Patient(models.Model):
    lastname = models.CharField(verbose_name='Фамилия', max_length=32)
    firstname = models.CharField(verbose_name='Имя', max_length=32)
    middlename = models.CharField(verbose_name='Отчество', max_length=32, blank=True)
    address = models.CharField(verbose_name='Адрес', max_length=64, blank=True, null=True)
    snils = models.CharField(verbose_name='Должность', max_length=14, blank=True, null=True)
    mobile_phone = models.BigIntegerField(verbose_name='мобильный телефон', blank=True, null=True)
    email = models.EmailField(verbose_name='email', blank=True, null=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='работает', default=True)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='создан', auto_now=True)

    def __str__(self):
        return f'{self.lastname} {self.firstname} {self.middlename}'


class Passport(models.Model):
    patient = models.ForeignKey(Patient, verbose_name='Пациент', related_name='patient', on_delete=models.CASCADE)
    series = models.IntegerField(verbose_name='Серия', max_length=4, blank=True)
    number = models.IntegerField(verbose_name='Серия', max_length=6, blank=True)
    issued = models.CharField(verbose_name='Кем выдан', max_length=256, blank=True)
    code = models.CharField(verbose_name='Код подразделения', max_length=7, blank=True, null=True)
    created = models.DateTimeField(verbose_name='выдан', blank=True)

