from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from accounts import views
from accounts.views import UserRegisterView, ProfileEditView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register_page'),
    path('login/', LoginView.as_view(template_name='accounts/login-page.html'), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include(
            [
                path('', views.details,name='account_details'),
                path('edit/', ProfileEditView.as_view(), name='edit_account'),
                path('delete/', views.delete, name='delete_account')
            ]
        )
    ),
]
