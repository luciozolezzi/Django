# Generated by Django 2.1.3 on 2018-12-18 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legajo', models.IntegerField()),
                ('nombre', models.CharField(max_length=140)),
                ('ingreso', models.TimeField(verbose_name='Horario de ingreso')),
                ('egreso', models.TimeField(verbose_name='Horario de egreso')),
            ],
        ),
        migrations.CreateModel(
            name='FaceRectangle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legajo', models.IntegerField()),
                ('top', models.IntegerField()),
                ('left', models.IntegerField()),
                ('width', models.IntegerField()),
                ('heigth', models.IntegerField()),
            ],
        ),
    ]
