from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add/<barang_id>/', views.add),
    path('<id>/update/', views.update),
    path('<id>/delete/', views.delete),
]
