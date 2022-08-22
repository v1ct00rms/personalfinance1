from django.shortcuts import render
from mainpage.forms import SaldoForm
from mainpage.models import Saldo

def home(request):
    return render(request, 'index.html')

def create(request):
    form = SaldoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data={}
    data['db'] = Saldo.objects.get(pk=pk)
    return render(request, 'index.html', data)

def edit(request, pk):
    data={}
    data['db'] = Saldo.objects.get(pk=pk)
    data['fatura'] = SaldoForm(instance=data['db'])
    return render(request, 'home', data)


def update(request, pk):

    data = {}
    data['db'] = Saldo.objects.get(pk=pk)
    form = SaldoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect ('home')

