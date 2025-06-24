from django.core.validators import MinLengthValidator
from django.db import models

from pets.models import Pet
from photos.validators import validate_field_size


# Create your models here.
class Photo(models.Model):

    photo = models.ImageField(
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
