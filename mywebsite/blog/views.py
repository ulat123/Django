# Views nya BLOG

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'judul': "joko",
        'kontribusi': "Supono",
    }
    return render(request, 'blog/index.html', context)

def cerita(request):
    context = {
        'judul': "Cerita",
        'kontribusi': "Mustajib Sip",
    }
    return render(request, 'blog/index.html', context)

def berita(request):
    context = {
        'judul': "Berita",
        'kontribusi': "Middle hand on Zay",
    }
    return render(request, 'blog/index.html', context)

def recent(request):
    # return HttpResponse('<h1>Ini adalah Recent Post.</h1>')
    context = {
        'judul': "Recent Post",
        'kontribusi': "Recent Post blog",
    }
    return render(request, 'blog/index.html', context)