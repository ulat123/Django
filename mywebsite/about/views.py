# Views nya About
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'judul':'Kelas tertutup | About',
        'subjudul':'Selamat datang',
    }
    return render(request, 'about/index.html', context)

def main(request):
    return HttpResponse('Ini adalah main about!')