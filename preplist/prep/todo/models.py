from django.db import models
from django.urls import reverse

DAYS = (
       ('Monday','Monday'),
       ('Tuesday','Tuesday'),
       ('Wednesday','Wednesday'),
       ('Thursday','Thursday'),
       ('Friday','Friday'),
       ('Saturday','Saturday'),
       ('Sunday','Sunday'),
       )

class PrepWork(models.Model):
    item = models.CharField(blank='False',max_length=200,)
    description = models.TextField(blank='False',help_text="Add instructions to remove any confusion. ", max_length=200)
    day_of_week = models.CharField(blank='False', max_length=20, choices=DAYS, help_text="Please set the day of week. ")

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('todo:prepwork-detail', kwargs={'id':self.id})

class Day(models.Model):
    day_of_week = models.ForeignKey('PrepWork',on_delete=models.CASCADE)

    def __str__(self):
        return self.day

    def get_absolute_url(self):
        return reverse('todo:prepwork_dayview', kwargs={'day_of_week':self.day_of_week})
