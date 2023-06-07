from django import forms
from products.widgets import CustomClearableFileInput
from products.models import Product, Category


class VendorProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'style', 'sku', 'price',)

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
       