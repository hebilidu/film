from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', views.accounts, name = 'accounts')
]