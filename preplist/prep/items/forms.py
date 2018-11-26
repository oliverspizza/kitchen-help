from django.forms import ModelForm
from items.models import Product

class OrderForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name',
                  'order_amount',
                  'par_amount',
                  'price',
        ]
