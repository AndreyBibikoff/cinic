from django.db import models


class Patient(models.Model):
    Yes = 'Y'
    No = 'N'
    Card_CHOICES = (
        (Yes, 'Заведена'),
        (No, 'Не заведена'),
    )
    Man = 'M'
    Woman = 'W'
    SEX_CHOICES = (
        (Man, 'Мужской'),
        (Woman, 'Женский'),
    )
    medical_card = models.CharField(verbose_name='Медицинская карта', max_length=1, choices=Card_CHOICES, default='N')
    sex = models.CharField(verbose_name='Пол', max_length=1, choices=SEX_CHOICES, blank=True)
    lastname = models.CharField(verbose_name='Фамилия', max_length=32)
    firstname = models.CharField(verbose_name='Имя', max_length=32)
    middlename = models.CharField(verbose_name='Отчество', max_length=32, blank=True)
    bdate = models.DateField(verbose_name='День рождения', blank=True, null=True, default='0001-01-01')
    address = models.CharField(verbose_name='Адрес', max_length=64, blank=True, null=True)
    snils = models.CharField(verbose_name='СНИЛС', max_length=14, blank=True, null=True)
    mobile_phone = models.BigIntegerField(verbose_name='мобильный телефон', blank=True, null=True)
    email = models.EmailField(verbose_name='email', blank=True, null=True)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='создан', auto_now=True)
    passp_series = models.IntegerField(verbose_name='Паспорт серия', blank=True)
    passp_number = models.IntegerField(verbose_name='Паспорт номер', blank=True)
    passp_issued = models.CharField(verbose_name='Кем выдан', max_length=256, blank=True)
    date_of_issue = models.DateField(verbose_name='Дата выдачи', blank=True)
    passp_code = models.CharField(verbose_name='Код подразделения', max_length=7, blank=True, null=True)

    def __str__(self):
        return f'{self.lastname} {self.firstname} {self.middlename}'


class PatientComments(models.Model):
    comment = models.TextField(verbose_name='Комментарий', blank=True)
    patient_comment = models.ForeignKey(Patient, related_name='comment', on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='Добавлен', auto_now_add=True)

    def __str__(self):
        return self.comment
