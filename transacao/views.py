from django.shortcuts import render, redirect
from transacao.forms import TransacaoForm
from mainpage.models import Transacao, Categoria, Fatura
from dateutil.relativedelta import relativedelta

def transacao(request):
    data = {}
    data['db'] = Transacao.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'transacao.html', {'categorias':categorias,'transacoes':data['db']})


def create(request):

    date_after_month = datetime.today() + relativedelta(months=1)

    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        aux = form.instance.data
        aux = aux.replace(day=1)

        for i in range(form.instance.parcelas):

            atualfatura = Fatura.objects.filter(data=aux)

            if not atualfatura.exists():
                atualfatura = Fatura(data=aux, valor=0)

            atualfatura = atualfatura.first()
            atualfatura.valor = atualfatura.valor + form.instance.valor
            atualfatura.save()
        form.instance.atualparcela=1
        form.instance.fatura = atualfatura
        form.save()
        return transacao(request)

def view(request, pk):
    data={}
    data['db'] = Transacao.objects.get(pk=pk)
    return render(request, 'transacao.html', data)

def edit(request, pk):
    data={}
    data['db'] = Transacao.objects.get(pk=pk)
    data['transacao'] = CategoriaForm(instance=data['db'])
    return render(request, 'home', data)


def update(request, pk):

    data = {}
    data['db'] = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect ('home')

def delete(request, pk):
    db = Transacao.objects.get(pk=pk)
    db.delete()
    return transacao(request)