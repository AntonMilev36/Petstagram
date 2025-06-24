from django.contrib import admin

from photos.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        'publication_date',
        'description',
        'get_tagged_pets'
    ]

    @staticmethod
    def get_tagged_pets(obj):
        return ', '.join(
            p.name for p in obj.tagged_pet.all()
        )
