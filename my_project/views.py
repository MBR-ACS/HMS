from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import statictics

'''
def welcome(request):
    return HttpResponse("Hello welcome to my website.")
''' 

def welcome(request):
    data = statictics()
    return render(request, 'welcome.html', context=data)