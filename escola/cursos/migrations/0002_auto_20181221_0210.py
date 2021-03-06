# Generated by Django 2.1.4 on 2018-12-21 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='professor',
            options={'verbose_name_plural': 'Professores'},
        ),
        migrations.AlterField(
            model_name='curso',
            name='valor',
            field=models.CharField(max_length=8, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='valor_hora',
            field=models.CharField(max_length=8, verbose_name='Valor da hora/aula'),
        ),
    ]
