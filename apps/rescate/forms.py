from django import forms
from apps.rescate.models import Producto

class formServicio(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'códigoProducto',
            'nombreProducto',
            'descripciónProducto',
            'precioProducto',
            'imagen',
        ]


        