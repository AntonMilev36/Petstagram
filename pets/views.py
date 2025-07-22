from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from common.form import CommentForm
from pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from pets.models import Pet


# Create your views here.

class PetAddView(CreateView):
    model = Pet
    form_class = PetCreateForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('account_details', kwargs={'pk': 1})

    def form_valid(self, form: PetCreateForm) -> HttpResponse:
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()
        return super().form_valid(form)


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs) -> dict:
        kwargs.update({
            'photos': self.object.photo_set.all(),
            'comment_form': CommentForm()
        })
        return super().get_context_data(**kwargs)


class PetEditView(UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self) -> str:
        return reverse_lazy(
            'pet_details',
            kwargs={
                'username': self.kwargs.get('username'),
                'pet_slug': self.kwargs.get('pet_slug')
            }
        )


class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    success_url = reverse_lazy('account_details', kwargs={'pk': 1})
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['form'] = PetDeleteForm(instance=self.object)
        return context
