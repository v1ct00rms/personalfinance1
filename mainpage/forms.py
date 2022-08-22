from django.forms import ModelForm
from mainpage.models import Saldo

class SaldoForm(ModelForm):
    class Meta:
        model = Saldo
        fields = ['saldo']
