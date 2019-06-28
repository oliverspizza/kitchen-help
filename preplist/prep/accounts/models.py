from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.validators import validate_even, validate_time_request
from django import forms


class Avaliablity(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE,default=None, help_text="Make sure you select your name.")
    not_available = models.DateField(help_text="You can only select one date per submit.",default=None)
    time_stamp = models.DateTimeField(auto_now_add=True,null=False,)

    def __str__(self):
        return str(self.person)

    # def clean_not_available(self):
    #     requested = self.cleaned_data.get("not_available")
    #     today = date.today()
    #     notice = timedelta(days=14)
    #     if requested <= (today + notice):
    #         print("can't request off")
    #         raise ValidationError("Request must be made two weeks in advance.")
    #     else:
    #         return requested

    def get_absolute_url(self):
        return reverse('accounts:avaliablity_delete', kwargs={'id':self.id})

'''
    -only allow 3 people to request a day off at a time.
    -add stmp server, with gmail account
'''
