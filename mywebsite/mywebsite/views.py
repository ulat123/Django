# Views nya Main Project mywebsite

from django.http import HttpResponse
from django.shortcuts import render

# methode view
def index(request):
    context = {
        # Tags Variable
        'judul' : 'Kelas tertutup | Home',
        'subjudul' : 'Selamat datang',

            # Tags Templates 
        'nav' : [
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
            ['/content','Content']
        ]
    }

    return render(request,'index.html', context)

def about(request):
    return render(request,'about.html')