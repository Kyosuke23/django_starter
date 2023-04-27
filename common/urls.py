from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import Menu, CommonLoginView, RegisterAccount

urlpatterns = [
    path('login/', CommonLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterAccount.as_view(), name='register'),
    path('', Menu.as_view(), name='menu'),
]
