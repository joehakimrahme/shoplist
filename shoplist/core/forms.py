from django.forms import ModelForm

from .models import Shopitem


class ShopitemForm(ModelForm):
    class Meta:
        model = Shopitem
        fields = ['name']
