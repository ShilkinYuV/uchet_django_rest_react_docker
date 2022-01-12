from django.db import models
from django.utils import timezone

class Cheludi (models.Model):
    FIO = models.CharField(max_length=100, verbose_name='ФИО')
    worked = models.BooleanField(default=True, verbose_name='Работает/Уволен')
    order = models.CharField(max_length=250, verbose_name='Приказ ввода вывода с удаленки')
    MOL = models.BooleanField(default=False)
    otdel_id = models.ForeignKey('Departments', on_delete=models.CASCADE)
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
    inventarnic = models.CharField(max_length=100, verbose_name='Инвентарный номер')
    state = models.CharField(choices=CHOICES_STATE, default='Введен в эксплуатацию', max_length=100, verbose_name='Состояние')
    price = models.CharField(max_length=100, verbose_name='Балансовая стоимость')  
    сommissioning_date = models.DateField(verbose_name='Дата ввода в эксплуатацию')
    FIO_ID = models.ForeignKey(Cheludi, related_name='chelud', on_delete=models.CASCADE, parent_link=True)
    MOL_ID = models.ForeignKey(Cheludi, related_name='mol', on_delete=models.CASCADE, parent_link=True)

    def __str__(self):
        return self.name
        
class Departments (models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование отдела')
    address = models.TextField(verbose_name='Адресс')

    def __str__(self):
        return self.name