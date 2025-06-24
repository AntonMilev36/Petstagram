from django.core.exceptions import ValidationError


def validate_field_size(image_object):
    if image_object.size > 5 * 1_024 * 1_024:
        raise ValidationError(
            "Image max size is 5MB"
        )
