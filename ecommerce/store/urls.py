from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('dashboard/', views.store, name="dashboard"),
    path('logout/', views.store, name="user-logout"),
    path('cart_summary/', views.store, name="cart-summary"),
    path('register/', views.store, name="register"),
    path('my_login/', views.store, name="my-login"),
    path('product/<slug:slug>/', views.product_info, name="product-info"),
]
