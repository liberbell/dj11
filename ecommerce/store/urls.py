from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('dashboard/', views.store, name="dashboard"),
]
