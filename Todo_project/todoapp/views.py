from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Todo

# Create your views here.
class HomeView(TemplateView):
    template_name = 'todoapp/home.html'
    

class TodoList(ListView):
    model = Todo
    context_object_name = 'tasks'

class TodoDetail(DetailView):
    model = Todo
    context_object_name = 'task'
    