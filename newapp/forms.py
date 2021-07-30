from django import forms
from .models import CrudUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CrudForm(forms.ModelForm):
    class Meta:
        model = CrudUser
        fields = ['first',
                  'last',
                  'short',
                  'title',
                  'email',
                  'contact_number',
                  'join_date',
                  'image_url',
                  'medium_url',
                  'thumbnail_url',

                  'team',
                  'job_title',

                  'loggedIn']


class CrudUpdateForm(forms.ModelForm):
    class Meta:
        model = CrudUser
        fields = ['first',
                  'last',
                  'short',
                  'title',
                  'email',
                  'contact_number',
                  'join_date',
                  'image_url',
                  'medium_url',
                  'thumbnail_url',

                  'team',
                  'job_title',

                  'loggedIn']
