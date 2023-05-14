from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Todo

# Create your views here.
class HomeView(TemplateView):
    template_name = 'todoapp/home.html'
    

class TodoList(ListView):
    model = Todo
    context_object_name = 'tasks'
    