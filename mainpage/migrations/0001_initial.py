# Generated by Django 3.1.4 on 2022-08-22 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Categoria')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('montante', models.DecimalField(decimal_places=2, max_digits=50, verbose_name='Valor total a ser gasto')),
            ],
        ),
        migrations.CreateModel(
            name='Fatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=50, verbose_name='Valor total da fatura')),
            ],
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=50, verbose_name='Valor da Transação')),
                ('data', models.DateField(verbose_name='Data')),
                ('parcelas', models.IntegerField(verbose_name='Parcelas')),
                ('atualparcela', models.IntegerField(default=None, verbose_name='Parcela Atual')),
                ('categoria', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='mainpage.categoria')),
                ('fatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fatura', to='mainpage.fatura')),
            ],
        ),
    ]
