from django import forms


class ShopitemForm(forms.Form):

    name = forms.CharField(max_length=100)
