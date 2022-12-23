from django.apps import AppConfig
from django.contrib import admin
from myapp1.models import Employee


class Myapp1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MyApp1'
class EmployeeAdmin(admin,modlesAdmin):
    list_display = ['empno','ename','job','sal','address'];
