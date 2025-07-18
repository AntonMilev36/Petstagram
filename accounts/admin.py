from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.forms import AppUserCreateForm

# Register your models here.

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(UserAdmin):
    fieldsets = [
        [None, {"fields": ("email", "password")}],
        [
            ("Permissions"),
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ],
            },
        ],
        [["Important dates"], {"fields": ["last_login"]}],
    ]

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    ordering = ("email",)
    list_display = ("email", "is_active", "is_staff")
    add_form = AppUserCreateForm
