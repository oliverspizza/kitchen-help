from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import SignUpForm, EditProfileForm, AvaliablityForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from accounts.models import Avaliablity
from django.contrib.auth.mixins import LoginRequiredMixin


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
    success_url = '/thanks/'

    def form_valid(self,form):
        return super().form_valid(form)

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
        return ('/thanks/')

# @login_required(login_url="/accounts/login/")
# def avaliablity_create(request):
#     if request.method == 'POST':
#         form = AvaliablityForm(request.POST)
#         if form.is_valid():
#             # save article to db
#             instance = form.save(commit=False)
#             instance.person = request.user
#             instance.save()
#             return redirect('accounts:profile')
#     else:
#         form = AvaliablityForm()
#     return render(request, 'accounts/avaliablity_form.html', { 'form': form })
