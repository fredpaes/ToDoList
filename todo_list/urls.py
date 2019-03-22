from django.urls import path
from .views import *

urlpatterns = [
    path('all', home, name = 'home'),
    path('add', AddView.as_view(), name='add'),
    path('delete/<int:todo_id>', supr, name='delete'),
    path('cross/<int:todo_id>', cross_on, name='cross'),
    path('uncross/<int:todo_id>', uncross, name='uncross'),
    path('edit/<int:todo_id>', EditView.as_view(), name='edit'),
]