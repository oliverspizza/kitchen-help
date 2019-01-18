from django.db import models
from django.contrib.auth.models import User

class Schedule(models.Model):
    day = models.DateField(help_text='Day of week')
    start_time = models.TimeField(help_text='Starting time')
    end_time = models.TimeField(help_text='End time')
    crew_member_name = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    deliver = models.BooleanField(default=False)

    def __str__(self):
        return str(self.crew_member_name)

# class Posititon(models.Model):
#     driver = models.models.ForeignKey(User, on_delete=models.CASCADE,default=None)
#     crew = models.models.ForeignKey(User, on_delete=models.CASCADE,default=None)
#     supervisor = models.models.ForeignKey(User, on_delete=models.CASCADE,default=None)
