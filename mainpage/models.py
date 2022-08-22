from django.db import models

class Saldo(models.Model):
    saldo = models.DecimalField('Valor da Renda Mensal', decimal_places=2, max_digits=50)

class Fatura(models.Model):
    data = models.DateField('Data')
    valor = models.DecimalField('Valor total da fatura', decimal_places=2, max_digits=50)

class Categoria(models.Model):
    nome = models.CharField('Categoria', max_length=100)
    descricao = models.CharField('Descrição', max_length=200)
    montante = models.DecimalField('Valor total a ser gasto', decimal_places=2, max_digits=50)

class Transacao(models.Model):
    valor = models.DecimalField('Valor da Transação', decimal_places =2, max_digits=50)
    data = models.DateField('Data')
    descricao = models.CharField('Descrição', max_length=100, default = None)
    parcelas = models.IntegerField('Parcelas')
    atualparcela = models.IntegerField('Parcela Atual', default = None)
    fatura =  models.ForeignKey(Fatura, on_delete=models.CASCADE, related_name='fatura')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default = None, related_name='categoria')