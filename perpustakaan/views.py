from django.shortcuts import render
from django.http import HttpResponse

def buku(request):
    return HttpResponse('<h1>Halaman Buku</h1>')

def penulis(request):
    return HttpResponse('Halaman Penulis')
