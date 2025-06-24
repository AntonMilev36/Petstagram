from django.contrib import admin

from common.models import Comment


# Register your models here.
@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    pass
