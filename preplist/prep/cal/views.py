from django.shortcuts import render
from django.views.generic.edit import FormView
from cal.forms import ScheduleForm

class ScheduleFromView(FormView):
    template_name = 'cal/create_schedule.html'
    form_class = ScheduleForm
    #success_url = 'create_schedule.html'
