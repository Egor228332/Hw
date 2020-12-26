from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def menu_categories(request):
    return HttpResponse('<h1>Hello world from MENU!</h1>')

def list_categories(request):
    context = {}
    return render(request, 'index.html', context=context)
