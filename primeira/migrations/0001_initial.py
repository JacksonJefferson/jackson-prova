# Generated by Django 2.2.4 on 2019-09-16 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarrinhoDeCompras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(max_length=50)),
                ('tamanho', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('sexo', models.CharField(max_length=1)),
                ('cpf', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('quantidade', models.IntegerField()),
                ('descricao', models.CharField(max_length=100)),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primeira.CarrinhoDeCompras')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primeira.Cliente')),
            ],
        ),
        migrations.AddField(
            model_name='carrinhodecompras',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primeira.Cliente'),
        ),
    ]
