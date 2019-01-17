from django import forms
from django.forms import ModelForm
from .models import Schedule
#from django.contrib.auth.models import User

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'
        widgets = {'day': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date',
            'type':'date'}),
            } #'start_time':forms.TimeInput(format='%H:%M.%P')
