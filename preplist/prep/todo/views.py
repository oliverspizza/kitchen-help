from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import PrepWork, DAYS
from .forms import PrepWorkForm
from django.views.generic.edit import FormView
from .filters import PrepWorkFilter
from django.contrib.auth.mixins import LoginRequiredMixin

class TodoList(ListView):
    queryset = PrepWork.objects.all()
    template_name = 'todo/prepwork_list.html'

class PrepWorkDetail(LoginRequiredMixin, DetailView):
    queryset = PrepWork.objects.all()
    template_name = 'todo/prepwork_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(PrepWork, id=id_)

class PrepCreate(LoginRequiredMixin, CreateView):
    form_class = PrepWorkForm
    template_name = 'todo/prepwork_form.html'
    success_url = '/thanks/'

    def form_valid(self,form):
        return super().form_valid(form)

class PrepUpdate(LoginRequiredMixin,UpdateView):
    model = PrepWork
    fields = ['item','description','day_of_week']
    template_name = 'todo/prepwork_form.html'

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(PrepWork, id=id)

class PrepDelete(LoginRequiredMixin,DeleteView):
    template_name = 'todo/prepwork_delete.html'
    #model = PrepWork

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(PrepWork, id=id)

    def get_success_url(self):
        return ('/thanks/')

def dailyprep(request):
    f = PrepWorkFilter(request.GET, queryset=PrepWork.objects.filter(day_of_week__icontains="day"))
    return render (request,'todo/dailyprep.html',{'filter':f})
