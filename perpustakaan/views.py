from django.shortcuts import render

def buku(request):
    return render(request, 'buku.html')

def penulis(request):
    return HttpResponse('Halaman Penulis')
