from django.shortcuts import render
from perpustakaan.models import Buku
from perpustakaan.form import FormBuku

def buku(request):
    page_title = 'Books'
    books = Buku.objects.all()
    # ? books = Buku.objects.filter(kelompok__nama='Produktif')[:2]

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

    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()

            form = FormBuku()
            datas = {
                'form': form,
                'page_title': page_title,
                'pesan': "Data berhasil disimpan"
            }
            return render(request, 'tambah_buku.html', datas)
    else:
        form = FormBuku()

        datas = {
            'form': form,
            'page_title': page_title,
        }

    return render(request, 'tambah_buku.html', datas)