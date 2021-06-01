from django.urls import path, include
from . import views

urlpatterns = [
    path('homepage/', views.FilmListView.as_view(), name = 'homepage'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category'),
    path('adddirector/', views.adddirector.as_view(), name = 'adddirector'),
    path('director/<int:pk>', views.DirectorDetailView.as_view(), name='director'),
    path('director/<int:pk>/update/', views.DirectorUpdateView.as_view(), name='updatedirector'),
    path('director/<int:pk>/delete/', views.DirectorDeleteView.as_view(), name='deletedirector'),
    path('addfilm/', views.addfilm.as_view(), name = 'addfilm'),
    path('film/<int:pk>', views.FilmDetailView.as_view(), name='film'),
    path('film/<int:pk>/update/', views.FilmUpdateView.as_view(), name='updatefilm'),
    path('film/<int:pk>/delete/', views.FilmDeleteView.as_view(), name='deletefilm')
]