from django.urls import path, include

from pets.views import PetAddView, PetDetailsView, PetEditView, PetDeleteView

urlpatterns = [
    path('add/', PetAddView.as_view(), name='add_pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
                path('', PetDetailsView.as_view(), name='pet_details'),
                path('edit/', PetEditView.as_view(), name='edit_pet'),
                path('delete/', PetDeleteView.as_view(), name='delete_pet'),
            ])
    )
]
