from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Avaliablity(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE,default=None, help_text="Make sure you select your name.")
    not_available = models.DateField(help_text="Date format must be typed like so: 2018-12-25",default=None)

    # def __str__(self):
    #     return self.person
    def get_absolute_url(self):
        return reverse('accounts:avaliablity_delete', kwargs={'id':self.id})

'''
    -add button for delete day request off / link (href) per querset id .
    -only allow 3 people to request a day off at a time.
    -add stmp server, with gmail account
'''
