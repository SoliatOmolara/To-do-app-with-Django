from django.urls import path
from .views import HomeView, TodoList, TodoDetail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tasks/', TodoList.as_view(),name='tasks'),
    path('details/<int:pk>/', TodoDetail.as_view(), name='details')
]
