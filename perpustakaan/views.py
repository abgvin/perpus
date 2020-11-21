from django.shortcuts import render
from perpustakaan.models import Buku

def buku(request):
    books = Buku.objects.all()

    datas = {
        'books': books,
    }

    return render(request, 'buku.html', datas)

def penerbit(request):
    title = 'Penerbit'

    datas = {
        'title' : title
    }
    return render(request, 'penerbit.html', datas)
