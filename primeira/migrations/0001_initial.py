# Generated by Django 2.2.4 on 2019-09-19 21:30

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
                ('cor', models.CharField(max_length=20)),
                ('tamanho', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('cpf', models.CharField(max_length=11)),
                ('sexo', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=50)),
                ('quantidade', models.IntegerField()),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primeira.CarrinhoDeCompras')),
            ],
        ),
        migrations.AddField(
            model_name='carrinhodecompras',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primeira.Cliente'),
        ),
    ]
