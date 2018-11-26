from django.urls import path

from items.views import ProductList, OrderFormView, ThanksPage

app_name = 'items'

urlpatterns = [
    path('product/',ProductList.as_view(), name='product'),
    path('order/',OrderFormView.as_view(), name='order'),
    path('thanks/',ThanksPage.as_view(), name='thanks'),
]
