# Generated by Django 2.1.4 on 2018-12-21 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0008_auto_20181221_1958'),
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
