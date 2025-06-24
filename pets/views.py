from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from pets.models import Pet


# Create your views here.
def add(request: HttpRequest) -> HttpResponse:
    form = PetCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(to='account_details', pk=1)

    context = {
        'form': form
    }

    return render(
        request,
        'pets/pet-add-page.html',
        context
    )

def details(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
    pet = Pet.objects.get(
        slug=pet_slug
    )
    photos = pet.photo_set.prefetch_related(
        "tagged_pet", 'like_set'
    ).all()

    context = {
        'pet': pet,
        'photos': photos
    }

    return render(
        request,
        'pets/pet-details-page.html',
        context=context
    )

def edit(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
    pet = Pet.objects.get(slug=pet_slug)
    form = PetEditForm(request.POST or None, instance=pet)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(to='pet_details', username=username, pet_slug=pet_slug)

    context = {
        'pet': pet,
        'form': form
    }

    return render(
        request,
        'pets/pet-edit-page.html',
        context
    )

def delete(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
    pet = Pet.objects.get(slug=pet_slug)
    form = PetDeleteForm(instance=pet)

    if request.method == 'POST':
        pet.delete()
        return redirect(to='account_details', pk=1)

    context = {
        'pet': pet,
        'form': form
    }

    return render(
        request,
        'pets/pet-delete-page.html',
        context
    )
