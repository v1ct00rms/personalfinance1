from django.shortcuts import render, redirect
from fatura.forms import FaturaForm
from mainpage.models import Fatura


def fatura(request):
    data = {}
    data['db'] = Fatura.objects.all()
    return render(request, 'fatura.html', {'faturas':data['db']})


def create(request):
    form = FaturaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data={}
    data['db'] = Fatura.objects.get(pk=pk)
    return render(request, 'fatura.html', data)

def edit(request, pk):
    data={}
    data['db'] = Fatura.objects.get(pk=pk)
    data['fatura'] = FaturaForm(instance=data['db'])
    return render(request, 'home', data)


def update(request, pk):

    data = {}
    data['db'] = Fatura.objects.get(pk=pk)
    form = FaturaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect ('home')

def delete(request, pk):
    db = Fatura.objects.get(pk=pk)
    db.delete()
    return redirect('home')