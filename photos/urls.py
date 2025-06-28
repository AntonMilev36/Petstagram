from django.urls import path, include

from photos import views
from photos.views import PhotoAddView, PhotoDetailView, PhotoEditView

urlpatterns = [
    path('add/', PhotoAddView.as_view(), name='add_photo'),
    path('<int:pk>', include([
                path('', PhotoDetailView.as_view(), name='photo_details'),
                path('edit/', PhotoEditView.as_view(), name='edit_photo'),
                path('delte/', views.delete, name='delete_photo')
            ])
    ),
]
