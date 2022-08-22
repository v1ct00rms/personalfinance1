from django.shortcuts import render, redirect
from categoria.forms import CategoriaForm
from mainpage.models import Categoria


def categoria(request):
    data = {}
    data['db'] = Categoria.objects.all()
    return render(request, 'categoria.html', {'categorias':data['db']})


def create(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return categoria(request)

def view(request, pk):
    data={}
    data['db'] = Categoria.objects.get(pk=pk)
    return render(request, 'categoria.html', data)

def edit(request, pk):
    data={}
    data['db'] = Categoria.objects.get(pk=pk)
    data['categoria'] = CategoriaForm(instance=data['db'])
    return render(request, 'home', data)


def update(request, pk):

    data = {}
    data['db'] = Categoria.objects.get(pk=pk)
    form = CategoriaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    print(form)
    return categoria(request)

def delete(request, pk):

    db = Categoria.objects.get(pk=pk)
    db.delete()
    return categoria(request)
