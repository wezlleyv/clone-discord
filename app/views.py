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
    server = Server.objects.filter(ID__exact=_id) # get a server 
    channels = Channels.objects.filter(id_to_server__exact=_id) # get channels about the server
    messages = Message.objects.filter(id_to_channel__exact=idChannel) # get messages about the channel
    CHactual = Channels.objects.filter(ID__exact=idChannel) # get channel about user in

    if _id == '1':
        server_users = User.objects.all() # if server equal Server Universal, get all users
    else:
        users = [] 
        server_users = server[0].user_in_server # get users in server
        server_users = json.loads(server_users)['users'] # load json
        for IDuser in server_users: # for for append users to list
            users.append(User.objects.filter(ID__exact=IDuser)[0])

        server_users = users 

    serverListUser = request.user.server_list_json # get user list server
    serverListUser = json.loads(serverListUser) # load jsons

    context = {} # prepare array
    context.update({
        'me': False, # me equal false for template
        'user': request.user, # send user info
        'server': server[0], # send server info
        'channels': channels, # send all channel in server
        'numberCH': len(channels), # send number about channels in server
        'room_name': idChannel, # send ID channel for script websocket
        'messages': messages, # send all messages about the channel
        'CHactual': CHactual[0], # send what channel user stay
        'serverls': serverListUser['server-list'], # send what server user in
        'users': server_users # send all users in server
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

@login_required(login_url="/login/")
def invite_server_view(request, serverId):
    server = Server.objects.filter(ID__exact=serverId)[0]

    users = json.loads(server.user_in_server)['users']

    if request.user.ID in users:
        return HttpResponseRedirect(f"/channels/{serverId}")

    context = {}
    context.update({
        "serverName": server.name,
        "serverPhoto": server.photo,
        "serverUsers": len(users),
    }
    )
    if request.method == "POST":
        user = request.user
        userServer = json.loads(user.server_list_json)['server-list']
        userServer.append(serverId)
        user.server_list_json = '''{"server-list": %s}''' % (userServer)
        user.save()
        
        users.append(user.ID)
        server.user_in_server = '''{"users": %s}''' % users
        server.save()


    return render(request, 'invite.html', context)

def redirect_view(request, _id):
    channels = Channels.objects.filter(id_to_server__exact=_id)
    return HttpResponseRedirect(f'{_id}/{channels[0].ID}')