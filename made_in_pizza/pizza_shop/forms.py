from django import forms
from django.forms import ModelForm
from pizza_shop.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['product', 'total_sum', 'start_date', 'end_date', 'status']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['city'].widget.attrs.update({'class': 'disable', 'disabled': ''})
        self.fields['street'].widget.attrs.update({'disabled': ''})
        self.fields['postal_code'].widget.attrs.update({'disabled': ''})
        self.fields['house_nr'].widget.attrs.update({'disabled': ''})
        self.fields['delivery_point'].widget.attrs.update({'disabled': ''})



