from django.shortcuts import render

def buku(request):
    title = 'Books List'
    books = ['Belajar Django', 'Belajar Web', 'Belajar Python']
    penulis = 'adam san'

    datas = {
        'title' : title,
        'book' : books,
        'penulis' : penulis,
    }

    return render(request, 'buku.html', datas)

def penerbit(request):
    title = 'Penerbit'

    datas = {
        'title' : title
    }
    return render(request, 'penerbit.html', datas)
