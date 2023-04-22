from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from channels.models import *

@login_required(login_url='/login/')
def my_view(request):
    name = Server.objects.all()
    context = {}
    context['me'] = True
    context['user'] = request.user
    context['server'] = name
    return render(request,'index.html', context)

@login_required(login_url='/login/')
def channel_view(request,_id):
    server = Server.objects.filter(ID__exact=_id)
    context = {}
    context['me'] = False
    context['user'] = request.user
    context['server'] = server[0]
    return render(request, 'index.html', context)