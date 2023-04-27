from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.contrib.auth.views import LoginView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


TEMPLATE_NAME_LOGIN = 'common/login.html'
TEMPLATE_NAME_REGISTER = 'common/register.html'
TEMPLATE_NAME_MENU = 'common/menu.html'
URL_NAME_MENU = 'menu'


class Menu(LoginRequiredMixin, TemplateView):
    template_name = TEMPLATE_NAME_MENU


class CommonLoginView(LoginView):
    fields = '__all__'
    template_name = TEMPLATE_NAME_LOGIN

    def get_success_url(self):
        return reverse_lazy(URL_NAME_MENU)


class RegisterAccount(FormView):
    template_name = TEMPLATE_NAME_REGISTER
    form_class = UserCreationForm
    success_url = reverse_lazy(URL_NAME_MENU)

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
