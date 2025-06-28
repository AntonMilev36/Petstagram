from django.urls import path, include

from common import views
from common.views import HomeView

urlpatterns = [
    path(
        '',
        HomeView.as_view(),
        name='home_page'
    ),
    path(
        '<int:photo_pk>/',
        include([
            path(
                'like/',
                views.like,
                name='like'
            ),
            path(
                'share/',
                views.share,
                name='share'
            ),
            path('comment/', views.comment, name='add-comment')
        ])
    )
]
