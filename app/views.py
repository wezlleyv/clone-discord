from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from channel.models import *
from accounts.models import *

import json

@login_required(login_url='/login/')
def app_view(request):
    name = Server.objects.all()
    context = {}

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
        server_users = User.objects.all()
    else:
        users = []
        server_users = server[0].user_in_server
        server_users = json.loads(server_users)['users']
        for IDuser in server_users:
            users.append(User.objects.filter(ID__exact=IDuser)[0])

        server_users = users

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
        'users': server_users
        })
    
    return render(request, 'index.html', context)

@login_required(login_url='/login/')
def create_server_view(request):
    if request.method == 'POST':
        user = request.user # get user info

        newServerName = request.POST['nameserver'] # get a name of server with method POST
        newServer = Server(name=newServerName) # create object Server
        
        serverInUser = newServer.user_in_server # get actually user in server
        serverInUserJson = json.loads(serverInUser) # load json with string
        serverInUserJson['users'].append(user.ID) # add new user for this server

        newServer.user_in_server = '''{"users": %s}''' % (serverInUserJson['users']) # concatenate for send for DB

        newServer.save() # save a new Server

        firstChannel = Channels(name="Chat geral", id_to_server=newServer.ID) # create a default channel
        firstChannel.save() # save a new Channel


        serverListJson = user.server_list_json # get a server list of user
        serverListJson = json.loads(serverListJson) # load json
        serverListJson["server-list"].append(newServer.ID) # add a new server for user
        user.server_list_json = '''{"server-list": %s }''' % (serverListJson['server-list']) # concatenate and send for DB
        user.save() # save info of user

        return HttpResponseRedirect(f"/channels/{newServer.ID}") # redirect for a new server



def redirect_view(request, _id):
    channels = Channels.objects.filter(id_to_server__exact=_id)
    return HttpResponseRedirect(f'{_id}/{channels[0].ID}')