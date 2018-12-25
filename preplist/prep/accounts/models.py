from django.db import models
from django.contrib.auth.models import User


class Avaliablity(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE,default=None, help_text="Make sure you select your name.")
    not_available = models.DateField(help_text="Date format must be typed like so: 2018-12-25")
# need to attach user to Avaliablity, connteced to a model form datepicker.
    def __str__(self):
        return self.person


'''
    -need User(id) to authunicate/associate only that id.(id can only control CRUD for that id unless in admin section)
    -add button for delete day request off.
    -Need a new your time has been submitted "success_url" for avaliablity_form
    -only list days associated with that users profile(id).
    -only allow 3 people to request a day off at a time.
'''
