from django.contrib import admin
from django import forms
from .models import *

class CheludiAdmin(admin.ModelAdmin):
    list_display = ('FIO', 'department_id')

admin.site.register(Cheludi, CheludiAdmin)

class TechnicsAdmin(admin.ModelAdmin):
    list_display = ('name', 'serynic', 'inventarnic')

admin.site.register(Technics, TechnicsAdmin)

class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

admin.site.register(Departments, DepartmentsAdmin)
