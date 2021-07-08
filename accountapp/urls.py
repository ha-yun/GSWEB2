from django.urls import path

from accountapp.views import ha_world

app_name='accountapp'
urlpatterns = [
    path('ha_world/',ha_world,name="ha_world"),
]