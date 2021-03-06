from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Avaliablity
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date, timedelta, datetime


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
            )

    def save(self,commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
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
            'last_name'
            )

class AvaliablityForm(ModelForm):
    class Meta:
        model = Avaliablity
        fields = ['not_available']
        widgets = {'not_available': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'})}


    # def clean_not_available(self):
    #     today = datetime.today()
    #     tomorrow = today + timedelta(1)
    #     yesterday = today - timedelta(1)
    #     x = self.cleaned_data.get('not_available')
    #     y = Avaliablity.objects.filter(not_available__lte=today)
    #     if x is y:
    #         raise ValidationError("nope")
    #     print (y)
    #     return x
