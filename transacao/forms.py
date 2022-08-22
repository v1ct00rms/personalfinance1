from django.forms import ModelForm
from mainpage.models import Transacao

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['valor', 'data','descricao', 'parcelas', 'categoria']