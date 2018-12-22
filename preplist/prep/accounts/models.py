from django.db import models
from django.contrib.auth.models import User


class Avaliablity(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    not_available = models.DateField()
# need to attach user to Avaliablity, connteced to a model form datepicker.
    def __str__(self):
        return self.person


'''
    -need User(id) to authunicate/associate only that id.(id can only control CRUD for that id unless in admin section)
    -display requested time off in profile.html, add button for edit, add and delete.
    -only list days associated with that users profile(id).
    -only allow 3 people to request a day off at a time.
     
'''
