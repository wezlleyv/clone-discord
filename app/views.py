from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from channel.models import *
from accounts.models import *

import json

@login_required(login_url='/login/')
def app_view(request):
    name = Server.objects.all()
    context = {}

    # slj = server list json
    serverListUser = request.user.server_list_json
    serverListUser = json.loads(serverListUser)

    context.update({
        'me': True,
        'user': request.user,
        'server': name,
        'serverls': serverListUser['server-list'],
    })

    return render(request,'index.html', context)

@login_required(login_url='/login/')
def channel_view(request,_id, idChannel):
    server = Server.objects.filter(ID__exact=_id)
    channels = Channels.objects.filter(id_to_server__exact=_id)
    messages = Message.objects.filter(id_to_channel__exact=idChannel)
    CHactual = Channels.objects.filter(ID__exact=idChannel)

    if _id == '1':
        users = User.objects.all()
    else:
        users = None

    serverListUser = request.user.server_list_json
    serverListUser = json.loads(serverListUser)

    context = {}
    context.update({
        'me': False,
        'user': request.user,
        'server': server[0],
        'channels': channels,
        'numberCH': len(channels),
        'room_name': idChannel,
        'messages': messages,
        'CHactual': CHactual[0],
        'serverls': serverListUser['server-list'],
        'users': users
        })
    
    return render(request, 'index.html', context)

def redirect_view(request, _id):
    channels = Channels.objects.filter(id_to_server__exact=_id)
    return HttpResponseRedirect(f'{_id}/{channels[0].ID}')

@login_required(login_url='/login/')
def create_server_view(request):
    if request.method == 'POST':
        newServerName = request.POST['nameserver']
        newSever = Server(name=newServerName)
        newSever.save()

        firstChannel = Channels(name="Chat geral", id_to_server=newSever.ID)
        firstChannel.save()

        user = request.user
        serverListJson = user.server_list_json
        serverListJson = json.loads(serverListJson)
        serverListJson["server-list"].append(newSever.ID)
        user.server_list_json = '''{"server-list": %s }''' % (serverListJson['server-list'])
        user.save()

        return HttpResponseRedirect(f"/channels/{newSever.ID}")