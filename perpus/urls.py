from django.contrib import admin
from django.urls import path
from perpustakaan.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('penerbit/', penerbit, name='penerbit'),
    path('buku/', buku, name='buku'),
    path('buku/tambah/', tambah_buku, name='tambah_buku'),
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
]