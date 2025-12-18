from django.shortcuts import render
from apps.nurses.models import Nurses

# Create your views here.
def list_nurses(request):
    data = Nurses.objects.all()
    return render(request, 'nurses/list_nurses.html', context={"nurses": data})