from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import PrepWork, DAYS
from .forms import PrepWorkForm
from django.views.generic.edit import FormView
from .filters import PrepWorkFilter

class TodoList(ListView):
    queryset = PrepWork.objects.all()
    template_name = 'todo/prepwork_list.html'

# class DayList(ListView):
#     queryset = PrepWork.objects.order_by('day_of_week')
#     template_name = 'todo/prepwork_dayview.html'
    #context = PrepWork.objects.filter(day_of_week__icontains="day")



class PrepWorkDetail(DetailView):
    queryset = PrepWork.objects.all()
    template_name = 'todo/prepwork_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(PrepWork, id=id_)

class PrepWorkFormView(FormView):
    form_class = PrepWorkForm
    template_name = 'todo/prep_work.html'
    success_url = '/thanks/'

    def form_valid(self,form):
        #print(self.request.POST['item'])
        return super(PrepWorkFormView,self).form_valid(form)

class PrepCreate(CreateView):
    form_class = PrepWorkForm
    template_name = 'todo/prepwork_form.html'
    queryset = PrepWork.objects.all()
    success_url = '/thanks/'

    def form_valid(self,form):
        #print(form.cleaned_data)
        return super().form_valid(form)

class PrepUpdate(UpdateView):
    model = PrepWork
    fields = ['item','description','day_of_week']
    template_name = 'todo/prepwork_form.html'

class PrepDelete(DeleteView):
    template_name = 'todo/prep_work.html'
    model = PrepWork
    success_url = reverse_lazy('TodoList')

def dailyprep(request):
    f = PrepWorkFilter(request.GET, queryset=PrepWork.objects.filter(day_of_week__icontains="day"))
    return render (request,'todo/dailyprep.html',{'filter':f})
