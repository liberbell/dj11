from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('dashboard/', views.store, name="dashboard"),
    path('cart_summary/', views.store, name="cart-summary"),
    path('register/', views.store, name="register"),
    path('product/<slug:product_slug>/', views.product_info, name="product-info"),
    path('search/<slug:category_slug>/', views.list_category, name="list-category"),
]
