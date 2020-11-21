from django.shortcuts import render
from perpustakaan.models import Buku

def buku(request):
    page_title = 'Books'
    books = Buku.objects.all()

    datas = {
        'page_title': page_title,
        'books': books,
    }

    return render(request, 'buku.html', datas)

def penerbit(request):
    title = 'Penerbit'

    datas = {
        'title' : title
    }
    return render(request, 'penerbit.html', datas)
