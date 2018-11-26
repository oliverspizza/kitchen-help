from django.shortcuts import render, redirect
from .models import Product
from .forms import OrderForm
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

class ProductList(ListView):
    model = Product
    template_name = 'items/product_list.html'


class OrderFormView(FormView):
    form_class = OrderForm
    template_name = 'items/order_form.html'
    success_url = '/thanks/'

    def form_valid(self,form):
        print(self.request.POST['product_name'])
        return super(OrderFormView,self).form_valid(form)

class ThanksPage(TemplateView):
    template_name = "items/thanks.html"

# def OrderFormView(request):
#     form = OrderForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = OrderForm()
#
#     context = {
#         'form':form
#     }
#     return render(request,'items/order_form.html', context)
