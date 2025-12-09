from django.http import HttpResponse

def products(request):
    prod = ['pen', 'mouse', 'car', 'mobile']
    return HttpResponse(f"my products = {prod}")

def friends(request, idx):
    try:
        names = ['hari', 'pavan', 'sunil']
        var = names[idx]
        return HttpResponse(f'my friend name is = {var}')
    except IndexError:
        return HttpResponse("Something went wrong.......!!!")

def welcome(request):
    return HttpResponse("Hello welcome to my website.")