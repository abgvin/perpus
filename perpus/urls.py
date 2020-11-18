from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def buku(request):
    return HttpResponse('Halaman Buku')

def penulis(request):
    return HttpResponse('Halaman Penulis')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku),
    path('penulis/', penulis),
]
