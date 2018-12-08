from django.views.generic.base import TemplateView

class HomPageView(TemplateView):
    template_name = 'items/home.html'
