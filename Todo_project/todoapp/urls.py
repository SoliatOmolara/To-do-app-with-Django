from django.urls import path
from .views import HomeView, TodoList, TodoDetail, TodoCreate, TodoUpdate

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tasks/', TodoList.as_view(),name='tasks'),
    path('details/<int:pk>/', TodoDetail.as_view(), name='details'),
    path('details/create/', TodoCreate.as_view(), name='create'),
    path('details/update/<int:pk>', TodoUpdate.as_view(), name='update')
]
