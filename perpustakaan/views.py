from django.shortcuts import render

def buku(request):
    judul = ['Belajar Django', 'Belajar Web', 'Belajar Python']
    penulis = 'adam san'

    konteks = {
        'title' : judul,
        'penulis' : penulis,
    }

    return render(request, 'buku.html', konteks)
