# Generated by Django 4.0.5 on 2022-06-07 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_funcionario_alter_genero_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filme',
            options={'ordering': ('titulo',)},
        ),
    ]
