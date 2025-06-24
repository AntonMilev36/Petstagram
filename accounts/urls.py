from django.urls import path, include

from accounts import views

urlpatterns = [
    path(
        'register/',
        views.register,
        name='register_page'
    ),
    path(
        'login/',
        views.login,
        name='login_page'
    ),
    path(
        'profile/<int:pk>/',
        include(
            [
                path(
                '',
                views.details,
                name='account_details'
                ),
                path(
                    'edit/',
                    views.edit,
                    name='edit_account'
                ),
                path(
                    'delete/',
                    views.delete,
                    name='delete_account'
                )
            ]
        )
    ),
]
