from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_in, name = 'login'),
    path('logout', views.log_out, name = 'logout'),
]