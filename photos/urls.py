from django.urls import path, include

from photos import views

urlpatterns = [
    path(
        'add/',
        views.add,
        name='add_photo'
    ),
    path(
        '<int:pk>',
        include(
            [
                path('', views.details, name='photo_details'),
                path('edit/', views.edit, name='edit_photo'),
                path('delte/', views.delete, name='delete_photo')
            ]
        )
    ),
]
