from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, resolve_url
from django.views.generic import ListView

from common.form import CommentForm, SearchFild
from common.models import Like
from photos.models import Photo

from pyperclip import copy


# Create your views here.
class HomeView(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos'

    def get_context_data(self, *, object_list: list=None, **kwargs):
        kwargs.update({
            'comment_form': CommentForm(),
            'search': SearchFild()
        })
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        pet_name = self.request.GET.get('pet_name')

        if pet_name:
            queryset = queryset.filter(
                tagged_pet__name__icontains=pet_name
            )

        return queryset


def like(request: HttpRequest, photo_pk: int) -> HttpResponse:
    like_obj = Like.objects.filter(
        to_photo_id=photo_pk,
        user=request.user
    ).first()

    if like_obj:
        like_obj.delete()
    else:
        Like.objects.create(
            to_photo_id=photo_pk,
            user=request.user
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
        comments.user = request.user
        comments.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_pk}')
