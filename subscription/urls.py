from django.urls import path, path
from . import views
from .views import Register, Login

urlpatterns = [
    path('', views.home, name='index'),
    path('login/', views.signin, name='login'),
    path('home/', views.index, name='home'),
    path('check-mail-ajax/', views.check_mail_ajax, name='check_mail_ajax'),
    path('register/', Register.as_view(), name='register'),
    path('login-req/', Login.as_view(), name='login_ajax'),
]
