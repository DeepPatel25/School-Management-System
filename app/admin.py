from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class UserModel(UserAdmin):
    list_display = ['username', 'user_type']


# Register your models here.
admin.site.register(CustomUser, UserModel)
admin.site.register(Standard)
admin.site.register(Session_Year)
admin.site.register(Student)
admin.site.register(Staff)
