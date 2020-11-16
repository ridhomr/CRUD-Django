from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('katalog.urls')),
    path('barang/', include('barang.urls')),
    path('keranjang/', include('keranjang.urls')),
    path('admin/', admin.site.urls),
]
