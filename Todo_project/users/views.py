from django.contrib.auth import login 
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import RegisterForm


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    redirect_autheticated_user = True
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
 
class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')
    
    def form_invalid(self, form):
        messages.error(self.request, "Invalid Username or Password")
        return self.render_to_response(self.get_context_data(form=form))