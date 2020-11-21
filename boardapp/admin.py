from django.contrib import admin
from .models import BoardModel, CustomUserModel

# Register your models here.
mymodels = [BoardModel, CustomUserModel]
admin.site.register(mymodels)