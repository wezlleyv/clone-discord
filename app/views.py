from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth.decorators import login_required

from channel.models import *

@login_required(login_url='/login/')
def my_view(request):
    name = Server.objects.all()
    context = {}

    context.update({
        'me': True,
        'user': request.user,
        'server': name,
    })

    return render(request,'index.html', context)

@login_required(login_url='/login/')
def channel_view(request,_id, idChannel):
    server = Server.objects.filter(ID__exact=_id)
    channels = Channels.objects.filter(id_to_server__exact=_id)
    messages = Message.objects.filter(id_to_channel__exact=idChannel)

    print(f"aaaaaaa {messages}")

    context = {}
    context.update({
        'me': False,
        'user': request.user,
        'server': server[0],
        'channels': channels,
        'numberCH': len(channels),
        'room_name': idChannel,
        'messages': messages,
        })
    
    return render(request, 'index.html', context)

def test_view(request):
    chanels = Message.objects.all()
    return HttpResponse(chanels[1])