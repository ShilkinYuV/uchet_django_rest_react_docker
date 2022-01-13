from django.contrib import admin
from django import forms
from .models import Attribute, TypeTechnics, UserProfile,Cheludi,Technics,Departments, ValueAttribute
from django.forms import ModelChoiceField, ModelForm

class CheludiAdmin(admin.ModelAdmin):
    list_display = ('FIO', 'department_id')

admin.site.register(Cheludi, CheludiAdmin)

class TechnicsAdmin(admin.ModelAdmin):
    list_display = ('name', 'serynic', 'inventarnic')
    

admin.site.register(Technics, TechnicsAdmin)

admin.site.register(Attribute)
admin.site.register(TypeTechnics)
admin.site.register(ValueAttribute)

class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

admin.site.register(Departments, DepartmentsAdmin)

admin.site.register(UserProfile)


