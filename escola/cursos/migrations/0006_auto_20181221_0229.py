# Generated by Django 2.1.4 on 2018-12-21 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0005_auto_20181221_0218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='turma',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='turma',
            name='professor',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Professor',
        ),
        migrations.DeleteModel(
            name='Turma',
        ),
    ]
