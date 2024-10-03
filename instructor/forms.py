from django import forms
from .models import Instractor


class InstractorForm(forms.ModelForm):
    class Meta:
        model = Instractor
        fields = [
            'name', 'email', 'instractor_id', 'excluci', 
            'education', 'phone_number', 'date_of_birth', 
            'bio', 'country', 'possiton', 'linkdlen_id', 'image'
        ]

class InstractorUpdateForm():
    class Meta:
        model = Instractor
        fields = [ 'name', 'email', 'instractor_id', 'excluci', 
            'education', 'phone_number', 'date_of_birth', 
            'bio', 'country', 'possiton', 'linkdlen_id', 'image']

# class UserDeleteForm(forms.ModelForm):
#     class Meta:
#         model = Instractor
#         fields = []