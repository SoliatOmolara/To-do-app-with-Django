from django.urls import path
from .views import HomeView, TodoList

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tasks/', TodoList.as_view(),name='tasks'),
]
