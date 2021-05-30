from django.urls import path, include
from . import views

urlpatterns = [
    path('homepage/', views.FilmListView.as_view(), name = 'homepage'),
    path('adddirector/', views.adddirector.as_view(), name = 'adddirector'),
    path('addfilm/', views.addfilm.as_view(), name = 'addfilm')
]