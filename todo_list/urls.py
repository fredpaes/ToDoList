from django.urls import path
from . import views

urlpatterns = [
    path('all', views.home, name = 'home'),
    path('add', views.add, name='add'),
    path('delete/<int:todo_id>', views.supr, name='delete'),
    path('cross/<int:todo_id>', views.cross_on, name='cross'),
    path('uncross/<int:todo_id>', views.uncross, name='uncross'),
    path('edit/<int:todo_id>', views.edit, name='edit'),
]