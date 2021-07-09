from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('new_search',views.new_search,name ='new_search'),
    path(r'^weather/',views.weather,name = 'weather'),
    path(r'^caloriemeter/',views.calorie_meter, name = 'caloriemeter'),
    path('text_to_html',views.text_to_html, name='text_to_html'),
    path('todo/',views.todo, name = 'todo'),
    path('todo/update_todo/<int:pk>/', views.update_todo, name= "update_todo"),
    path('todo/delete/<int:pk>/',views.delete_todo,name="delete_todo"),
]