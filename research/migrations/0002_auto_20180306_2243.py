# Generated by Django 2.0.2 on 2018-03-06 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='article',
            table='Article',
        ),
        migrations.AlterModelTable(
            name='bangmok',
            table='Bangmok',
        ),
        migrations.AlterModelTable(
            name='figures',
            table='figures',
        ),
        migrations.AlterModelTable(
            name='records',
            table='records',
        ),
    ]
