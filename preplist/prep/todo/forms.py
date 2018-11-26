from django.forms import ModelForm
from todo.models import PrepWork

class PrepWorkForm(ModelForm):
    class Meta:
        model = PrepWork
        fields = ['item','description','day_of_week']
