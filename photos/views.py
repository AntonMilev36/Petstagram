from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from common.models import Comment
from photos.forms import PhotoCreateForm, PhotoEditForm
from photos.models import Photo


# Create your views here.
def add(request: HttpRequest) -> HttpResponse:
    form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home_page')

    context = {
        'form': form
    }

    return render(
        request,
        template_name='photos/photo-add-page.html',
        context=context
    )

def details(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    comments = Comment.objects.filter(
        to_photo_id=pk
    )

    context = {
        'photo': photo,
        'comments': comments
    }

    return render(
        request,
        template_name='photos/photo-details-page.html',
        context=context
    )

def edit(request: HttpRequest, pk: int) -> HttpResponse:
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, instance=photo)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('photo_details', pk=pk)

    context = {
        'form': form,
        'photo': photo
    }

    return render(
        request,
        template_name='photos/photo-edit-page.html',
        context=context
    )

def delete(request: HttpRequest, pk: int) -> HttpResponse:
    photo = Photo.objects.get(pk=pk)
    photo.delete()

    return redirect('home_page')
