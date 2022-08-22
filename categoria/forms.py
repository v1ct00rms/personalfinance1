from django.forms import ModelForm
from mainpage.models import Categoria

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao', 'montante']