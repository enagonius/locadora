# Generated by Django 4.0.5 on 2022-06-07 04:27

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0003_alter_direcao_unique_together_remove_direcao_diretor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='genero',
            options={'verbose_name': 'Gênero', 'verbose_name_plural': 'Gêneros'},
        ),
        migrations.RemoveField(
            model_name='aluguel',
            name='datetime_devolucao',
        ),
    ]
