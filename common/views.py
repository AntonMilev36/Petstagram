from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, resolve_url

from common.models import Like
from photos.models import Photo

from pyperclip import copy


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    all_photos = Photo.objects.all()

    context = {
        'all_photos': all_photos
    }

    return render(
        request,
        template_name='common/home-page.html',
        context=context
    )

def like(request: HttpRequest, photo_pk: int) -> HttpResponse:
    like_obj = Like.objects.filter(
        to_photo_id=photo_pk
    ).first()

    if like_obj:
        like_obj.delete()
    else:
        Like.objects.create(
            to_photo_id=photo_pk
        )

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_pk}')

def share(request: HttpRequest, photo_pk: int) -> HttpResponse:
    #pyperclip copy functionality

    copy(request.META['HTTP_HOST'] + resolve_url('photo_details', photo_pk))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_pk}')


