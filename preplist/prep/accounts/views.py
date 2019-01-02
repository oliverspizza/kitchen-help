from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import SignUpForm, EditProfileForm, AvaliablityForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from accounts.models import Avaliablity
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date
from accounts.filters import AvaliablityFilter


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('todo:dailyprep')
    else:
        form = SignUpForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('todo:dailyprep')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)


def profile(request):
    user = request.user
    day_off  = Avaliablity.objects.filter(person=request.user)
    args = {'user':user, 'day_off':day_off}
    return render(request,'accounts/profile.html',args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request,'accounts/edit_profile.html',args)

class AvaliablityCreate(LoginRequiredMixin, CreateView):
    form_class = AvaliablityForm
    template_name = 'accounts/avaliablity_form.html'
    success_url = '/accounts/avaliablity_confirm/'

    def form_valid(self,form):
        form.instance.person = self.request.user
        return super().form_valid(form)

def available(request):
    f = AvaliablityFilter(request.GET, queryset=Avaliablity.objects.all())
    return render (request,'accounts/avafilter.html',{'filter':f})

class AvaliablityUpdate(LoginRequiredMixin,UpdateView):
    model = Avaliablity
    fields = ['person','not_available']
    template_name = 'todo/prepwork_form.html'

class AvaliablityDelete(LoginRequiredMixin,DeleteView):
    template_name = 'accounts/avaliablity_delete.html'

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Avaliablity, id=id)

    def get_success_url(self):
        return ('/accounts/profile/')

class AvaliablityConfirm(TemplateView):
    template_name = "accounts/avaliablity_confirm.html"


def old_post(request):
    days = Avaliablity.objects.date('not_available','year')
    print (days)
    return render(request,'accounts/profile.html',days)
