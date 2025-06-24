from django import forms

from pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ['slug']

        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Birth Date',
            'pet_photo': 'Link to Image'
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': "Enter your pet name:"
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': "date"
                }
            ),
            'pet_photo': forms.TextInput(
                attrs={
                    'placeholder': "Place URL to your pet image:"
                }
            ),
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(PetBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
