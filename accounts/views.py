from django.contrib.auth import get_user_model
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView
from accounts.models import Profile

from accounts.forms import AppUserCreateForm, ProfileEditForm

UserModel = get_user_model()

class UserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login_page')

    def form_valid(self, form: AppUserCreateForm) -> HttpResponse:
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        return response


# def details(request, pk:int):
#     return render(
#         request,
#         'accounts/profile-details-page.html'
#     )

class ProfileDetailsView(DetailView):
    model = Profile
    template_name =  'accounts/profile-details-page.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['likes_count'] = self.object.user.like_set.count()

        return context


class ProfileEditView(UpdateView):
    model = UserModel
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self) -> str:
        return reverse(
            'account_details',
            kwargs={'pk': self.object.pk}
        )

def delete(request, pk:int):
    return render(
        request,
        'accounts/profile-delete-page.html'
    )
