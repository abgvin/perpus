from django.contrib import admin
from django.urls import path
from perpustakaan.views import buku

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku),
]
