from django import forms

from .models import Product


class ProductForms(forms.ModelForms):
    class Meta:
        model=Product
        fields=["title","content","price","sale_price"]

