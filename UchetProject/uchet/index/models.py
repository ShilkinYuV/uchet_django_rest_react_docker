from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db.models.deletion import CASCADE


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Пользователь должен иметь пароль')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Создание и сохранение суперпользователя"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in this system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """"Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return '{name} ({email})'.format(name=self.name, email=self.email)


class Cheludi (models.Model):
    """Class людей владеющих техниками"""
    FIO = models.CharField(max_length=100, verbose_name='ФИО')
    WorksNow = models.BooleanField(
        default=True, verbose_name='Работает?')
    order = models.CharField(
        max_length=250, verbose_name='Приказ ввода вывода с удаленки')
    isItMOL = models.BooleanField(default=False, verbose_name='МОЛ?')
    department_id = models.ForeignKey(
        'Departments', on_delete=models.CASCADE, verbose_name='Отдел')
    cabinet = models.CharField(max_length=100, verbose_name='Кабинет')

    def __str__(self):
        return self.FIO


class TypeTechnics(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тип техники')

    def __str__(self):
        return self.name


class Attribute(models.Model):
    technics_type = models.ForeignKey(TypeTechnics, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class Technics (models.Model):
    """Class техники"""
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

    technics_type = models.ForeignKey(
        TypeTechnics, related_name='tech', on_delete=CASCADE)
    attribute = models.ManyToManyField(Attribute)
    value_id = models.ForeignKey('ValueAttribute',related_name='technics_value_attr', on_delete=CASCADE)
    
    def __str__(self):
        return self.name


class ValueAttribute(models.Model):
    value = models.CharField(max_length=255)
    attribute = models.ForeignKey(Attribute, on_delete=CASCADE)
    technics = models.ForeignKey(Technics, on_delete=CASCADE)
    
    def __str__(self):
        return self.value



class Departments (models.Model):
    """Class отделов"""
    name = models.CharField(max_length=250, verbose_name='Наименование отдела')
    address = models.TextField(verbose_name='Адресс')

    def __str__(self):
        return self.name
