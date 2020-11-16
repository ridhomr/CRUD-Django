from django.contrib import admin
from . import models

class KeranjangAdmin(admin.ModelAdmin):
  pass

admin.site.register(models.Keranjang, KeranjangAdmin)
