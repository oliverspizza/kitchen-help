from django.forms import ModelForm
from todo.models import PrepWork
from django import forms

class PrepWorkForm(ModelForm):
    class Meta:
        model = PrepWork
        fields = ['item','description','day_of_week']
        widgets = {'item':forms.TextInput(attrs={'placeholder':' Add Product Name'}),
                   'description':forms.Textarea(attrs={'placeholder':
                   'Give a breif description of what needs to be done for this item and how much for this day.'})
        }
