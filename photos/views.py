from django.shortcuts import render

from common.models import Comment
from photos.models import Photo


# Create your views here.
def add(request):
    return render(
        request,
        template_name='photos/photo-add-page.html'
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

def edit(request, pk: int):
    return render(
        request,
        template_name='photos/photo-edit-page.html'
    )