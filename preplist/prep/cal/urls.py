from django.urls import path, include
from cal.views import (
    ScheduleFromView,
)

app_name ='cal'

urlpatterns = [
    path('cal/schedule/',ScheduleFromView.as_view(),name='schedule')

]
