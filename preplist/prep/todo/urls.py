from django.urls import path
from . import views
from todo.views import (
    TodoList,
    PrepCreate,
    PrepUpdate,
    PrepDelete,
    PrepWorkFormView,
    PrepWorkDetail,
    #DayList,
    dailyprep,
)

app_name = 'todo'

urlpatterns = [
    path('todo/',TodoList.as_view(), name='prepwork-list'),
    path('toprep/',PrepWorkFormView.as_view(), name='toprep'),
    path('prepcreate/',PrepCreate.as_view(), name='prepcreate'),
    path('prepupdate/',PrepUpdate.as_view(), name='prepupdate'),
    path('prepdelete/',PrepDelete.as_view(), name='prepdelete'),
    path('<int:id>/',PrepWorkDetail.as_view(), name='prepwork-detail'),
    #path('<day_of_week>/',DayList.as_view(), name='prepwork_dayview'),
    path('dailyprep/', views.dailyprep,name='dailyprep'),

]
