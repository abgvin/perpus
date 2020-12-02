from django.shortcuts import render, redirect
from perpustakaan.models import Buku
from perpustakaan.form import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    page_title = 'Edit Buku'
    if request.POST:
        form = FormBuku(request.POST, request.FILES, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui!")
            return redirect('ubah_buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form':form,
            'buku':buku,
            'page_title':page_title,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    page_title = 'Books'
    books = Buku.objects.all()

    datas = {
        'page_title': page_title,
        'books': books,
    }

    return render(request, 'buku.html', datas)

@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
    title = 'Penerbit'

    datas = {
        'title' : title
    }
    return render(request, 'penerbit.html', datas)

@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    page_title = 'Tambah Buku'

    if request.POST:
        form = FormBuku(request.POST, request.FILES)
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

@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()

    messages.success(request, "Data berhasil dihapus")
    return redirect('buku')

@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User berhasil dibuat")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi kesalahan!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form': form,
        }
    
    return render(request, 'signup.html', konteks)

