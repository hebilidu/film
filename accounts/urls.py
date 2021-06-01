from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('', include('django.contrib.auth.urls'))
]