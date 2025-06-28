from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from common.models import Comment
from photos.forms import PhotoCreateForm, PhotoEditForm
from photos.models import Photo


# Create your views here.

class PhotoAddView(CreateView):
    model = Photo
    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('home_page')


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            to_photo_id=self.object.pk
        )
        return context


class PhotoEditView(UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = 'photos/photo-edit-page.html'

    def get_success_url(self) -> str:
        return reverse(
            'photo_details',
            kwargs={'pk': self.object.pk}
        )


def delete(request: HttpRequest, pk: int) -> HttpResponse:
    photo = Photo.objects.get(pk=pk)
    photo.delete()

    return redirect('home_page')
