from django.shortcuts import render
from perpustakaan.models import Buku
from perpustakaan.form import FormBuku

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

def tambah_buku(request):
    page_title = 'Tambah Buku'

    form = FormBuku()

    datas = {
        'form': form,
        'page_title': page_title,
    }

    return render(request, 'tambah_buku.html', datas)