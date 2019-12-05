from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=254, help_text="Eg xxx@gmail.com")


    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=false)
        user.first_name = self.cleaned['first_name']
        user.last_name = self.cleaned_data['email']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'

        )

