from django.contrib import admin
from . import models

@admin.register(models.LngDesc)
class LngDescAdmin(admin.ModelAdmin):
    list_display = ('loots', 'lang', 'name', 'description',
                    'meta_name', 'meta_description', 'keyboards')
