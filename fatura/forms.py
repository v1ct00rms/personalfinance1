from django.forms import ModelForm
from mainpage.models import Fatura

class FaturaForm(ModelForm):
    class Meta:
        model = Fatura
        fields = ['data', 'valor']
