import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import admin
from django.contrib import auth

from .models import Brand, Category, Product

# Register your models here.

admin.site.site_header = 'Admin Dashboard'


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.unregister(auth.models.Group)
admin.site.unregister(auth.models.User)
