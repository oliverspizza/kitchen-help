from django.urls import path
from . import views
from todo.views import (
    TodoList,
    PrepCreate,
    PrepUpdate,
    PrepDelete,
    PrepWorkDetail,
    dailyprep,
)

app_name = 'todo'

urlpatterns = [
    path('prepcreate/',PrepCreate.as_view(), name='prepcreate'),
    path('prepupdate/',PrepUpdate.as_view(), name='prepupdate'),
    path('<int:id>/prepdelete/',PrepDelete.as_view(), name='prepdelete'),
    path('<int:id>/',PrepWorkDetail.as_view(), name='prepwork-detail'),
    path('dailyprep/', views.dailyprep,name='dailyprep'),

]
