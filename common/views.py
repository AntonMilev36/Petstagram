from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, resolve_url

from common.form import CommentForm, SearchFild
from common.models import Like
from photos.models import Photo

from pyperclip import copy


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    comment_form = CommentForm()
    search = SearchFild(request.GET or None)

    if search.is_valid():
        all_photos = Photo.objects.filter(
            tagged_pet__name__icontains=search.cleaned_data['pet_name']
        )
    else:
        all_photos = Photo.objects.all()

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search': search
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

def comment(request: HttpRequest, photo_pk: int) -> HttpResponse:

    photo = Photo.objects.get(pk=photo_pk)
    form = CommentForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        comments = form.save(commit=False)
        comments.to_photo = photo
        comments.save()



    return redirect(request.META['HTTP_REFERER'] + f'#{photo_pk}')
