from django.db import models
from django.contrib.auth.models import User

class Schedule(models.Model):
    day = models.DateField(help_text='Day of week')
    start_time = models.TimeField(help_text='starting time')
    end_time = models.TimeField(help_text='end time')
    crew_member_name = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    position = models.BooleanField(delivery=True)


# class Posititon(models.Model):
#     driver = models.models.ForeignKey(User, on_delete=models.CASCADE,default=None)
#     crew = models.models.ForeignKey(User, on_delete=models.CASCADE,default=None)
#     supervisor = models.models.ForeignKey(User, on_delete=models.CASCADE,default=None)
