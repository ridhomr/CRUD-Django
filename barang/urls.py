from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('<id>/update', views.update),
    path('<id>/delete', views.delete),
]
