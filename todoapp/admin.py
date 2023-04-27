from django.contrib import admin
from todoapp.models import Task, Category

# Register your models here.
admin.site.register(Task)
admin.site.register(Category)
