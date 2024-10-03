from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import User


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'name', 'education', 'phone_number', 'address', 'image', 'user_type', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'education', 'phone_number', 'address', 'image', 'user_type']

class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []
