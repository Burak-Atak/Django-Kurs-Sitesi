from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm
from .forms import CustomAuthenticationForm
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


class LoginView(FormView):
    template_name = 'login.html'
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required(login_url='/accounts/login/')
def dashboard(request):
    pass
