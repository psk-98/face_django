from django import forms
from .models import User, UserImage


class UserForm(forms.ModelForm):
    name = forms.CharField(max_length=80)
    class Meta:
        model = User
        fields = ['name',]

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = UserImage
        fields = ['image']

class _UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name']


class UserFullForm(UserForm):
    images = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True}), required=False)

    class Meta(_UserForm.Meta):
        fields = _UserForm.Meta.fields + ['images']
