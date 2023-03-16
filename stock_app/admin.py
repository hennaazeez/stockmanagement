from django.contrib import admin

# Register your models here.
from stock_app import models

admin.site.register(models.Login)
admin.site.register(models.register)
admin.site.register(models.stock)

