from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_summary, name="cart-summary"),
    path('add/', views.cart_add, name="cart-add"),
    path('delete/<slug:slug>', views.cart_delete, name="cart-delete"),
    path('update/<slug:int>', views.cart_update, name="cart-update"),
]
