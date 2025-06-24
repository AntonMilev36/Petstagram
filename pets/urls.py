from django.urls import path, include

from pets import views

urlpatterns = [
    path(
        'add/',
        views.add,
        name='add_pet'
    ),
    path(
        '<str:username>/pet/<slug:pet_slug>/',
        include(
            [
                path(
                    '',
                    views.details,
                    name='pet_details'
                ),
                path(
                    'edit/',
                    views.edit,
                    name='edit_pet'
                ),
                path(
                    'delete/',
                    views.delete,
                    name='delete_pet'
                ),
            ]
        )
    )
]
