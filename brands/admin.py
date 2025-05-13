from django.contrib import admin
from . import models

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','name','description')
    search_fields = ('name',)
    ordering = ['id'] 

admin.site.register(models.Brand, BrandAdmin)