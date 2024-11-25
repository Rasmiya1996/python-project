from django.contrib import admin

# Register your models here.
from product_app import models

admin.site.register(models.Login)
admin.site.register(models.Customer)
admin.site.register(models.Category)
admin.site.register(models.Item)
admin.site.register(models.Quantity_1)
admin.site.register(models.Paymoney)
admin.site.register(models.Review)

