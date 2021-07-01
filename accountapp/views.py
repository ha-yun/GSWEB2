from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def ha_world(request):
    return render(request, 'accountapp/ha_world.html')