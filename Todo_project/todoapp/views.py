from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class HomeView(TemplateView):
    template_name = 'todoapp/home.html'
    

class TodoList(LoginRequiredMixin,ListView):
    model = Todo
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context

class TodoDetail(LoginRequiredMixin,DetailView):
    model = Todo
    context_object_name = 'task'
    
    def get_queryset(self):
        base_qs = super(TodoDetail, self).get_queryset()
        return base_qs.filter(user=self.request.user)  
    
class TodoCreate(LoginRequiredMixin,CreateView):
    model = Todo
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(TodoCreate, self).form_valid(form)
    
    
    
class TodoUpdate(LoginRequiredMixin,UpdateView):
    model = Todo
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was updated successfully.")
        return super(TodoUpdate, self).form_valid(form)
    
    def get_queryset(self):
        base_qs = super(TodoUpdate, self).get_queryset()
        return base_qs.filter(user=self.request.user)
    
class TodoDelete(LoginRequiredMixin,DeleteView):
    model = Todo
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    
    def form_valid(self,form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(TodoDelete, self).form_valid(form)
    
    def get_queryset(self):
        base_qs = super(TodoDelete, self).get_queryset()
        return base_qs.filter(user=self.request.user)