from django.http import HttpResponse
from django.shortcuts import render
from apps.dashboard.views import statictics
from django.contrib.auth.decorators import login_required

'''
def welcome(request):
    return HttpResponse("Hello welcome to my website.")
''' 
@login_required
def welcome(request):
    data = statictics()
    return render(request, 'welcome.html', context=data)