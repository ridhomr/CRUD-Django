from django.contrib import admin
from . import models

class BarangAdmin(admin.ModelAdmin):
  list_display = ['nama', 'harga']

admin.site.register(models.Barang, BarangAdmin)
