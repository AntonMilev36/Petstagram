from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Pet(models.Model):

    name = models.CharField(
        max_length=30
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    pet_photo = models.URLField()

    slug = models.SlugField(
        unique=True,
        blank=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
