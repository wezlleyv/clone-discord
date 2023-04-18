from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def my_view(request):
    context = {}
    context['user'] = request.user
    return render(request,'index.html', context)