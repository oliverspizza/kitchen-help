from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth import login, logout
from accounts.views import (
    AvaliablityCreate,
    AvaliablityConfirm,
    AvaliablityDelete,
    )
app_name ='accounts'

urlpatterns = [
    path('accounts/signup/', views.signup_view,name="signup"),
    path('login/', views.login_view,name="login"),
    path('logout/', views.logout_view,name="logout"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/',views.profile,name="profile"),
    path('accounts/edit_profile/',views.edit_profile,name="edit_profile"),
    path('accounts/avaliablity_create/',AvaliablityCreate.as_view(), name='avaliablity_create'),
    path('accounts/avaliablity_confirm/',AvaliablityConfirm.as_view(), name='avaliablity_confirm'),
    path('<int:id>/accounts/avaliablity_delete/',AvaliablityDelete.as_view(), name='avaliablity_delete'),
]
