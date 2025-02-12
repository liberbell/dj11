from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('email-verification/', views.email_verification, name="email-verification"),
]
