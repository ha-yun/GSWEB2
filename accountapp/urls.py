from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import ha_world, AccountCreateView

app_name='accountapp'
urlpatterns = [
    path('ha_world/',ha_world,name="ha_world"),

    path('login/', LoginView.as_view(templates='accountapp/login.html'), name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/',AccountCreateView.as_view(), name='create')
]