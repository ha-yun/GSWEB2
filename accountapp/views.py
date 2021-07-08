from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def ha_world(request):
    if request.method=='POST':
        temp = request.POST.get('hello_world_input')
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        return render(request, 'accountapp/ha_world.html',context={'hello_world_output':new_hello_world})
    else:
        return render(request, 'accountapp/ha_world.html',context={'text':'GET METHOD!'})