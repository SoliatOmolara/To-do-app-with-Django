from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')
    
    def form_invalid(self, form):
        messages.error(self.request, "Invalid Username or Password")
        return self.render_to_response(self.get_context_data(form=form))