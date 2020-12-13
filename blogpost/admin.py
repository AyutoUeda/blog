from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import SampleModel, BlogModel

# Register your models here.

admin.site.register(SampleModel)
admin.site.register(BlogModel)