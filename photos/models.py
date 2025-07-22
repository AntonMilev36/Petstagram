from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from pets.models import Pet
from photos.validators import validate_field_size


# Create your models here.

UserModel = get_user_model()

class Photo(models.Model):

    photo = models.ImageField(
        upload_to='files',
        validators=[
            validate_field_size
        ]
    )

    description = models.TextField(
        max_length=300,
        null=True,
        validators=[
            MinLengthValidator(10)
        ]
    )

    location = models.CharField(
        max_length=30
    )

    tagged_pet = models.ManyToManyField(
        to=Pet,
        blank=True
    )

    publication_date = models.DateField(
        auto_now=True
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        blank=True
    )

    def __str__(self):
        return ', '.join(
            p.name for p in self.tagged_pet.all()
        )
