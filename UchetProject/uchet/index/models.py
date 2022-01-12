from django.db import models
from django.utils import timezone


class Cheludi (models.Model):
    FIO = models.CharField(max_length=100, verbose_name='ФИО')
    WorksNow = models.BooleanField(
        default=True, verbose_name='Работает?')
    order = models.CharField(
        max_length=250, verbose_name='Приказ ввода вывода с удаленки')
    isItMOL = models.BooleanField(default=False, verbose_name='МОЛ?')
    department_id = models.ForeignKey('Departments', on_delete=models.CASCADE, verbose_name='Отдел')
    cabinet = models.CharField(max_length=100, verbose_name='Кабинет')

    def __str__(self):
        return self.FIO


class Technics (models.Model):
    CHOICES_STATE = (
        ('Введен в эксплуатацию', 'Введен в эксплуатацию'),
        ('Принят к учету', 'Принят к учету'),
    )

    name = models.CharField(max_length=250, verbose_name='Наименование')
    serynic = models.CharField(max_length=100, verbose_name='Серийный номер')
    inventarnic = models.CharField(
        max_length=100, verbose_name='Инвентарный номер')
    state = models.CharField(
        choices=CHOICES_STATE, default='Введен в эксплуатацию', max_length=100, verbose_name='Состояние')
    price = models.CharField(
        max_length=100, verbose_name='Балансовая стоимость')
    сommissioning_date = models.DateField(
        verbose_name='Дата ввода в эксплуатацию')
    # Держатель техники
    holder_id = models.ForeignKey(
        Cheludi, related_name='chelud', on_delete=models.CASCADE, parent_link=True)
    # Материально ответственное лицо(МОЛ) данной техники
    MOL_ID = models.ForeignKey(
        Cheludi, related_name='mol', on_delete=models.CASCADE, parent_link=True)

    def __str__(self):
        return self.name


class Departments (models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование отдела')
    address = models.TextField(verbose_name='Адресс')

    def __str__(self):
        return self.name
