# Generated by Django 4.2.2 on 2023-10-20 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PLAQUES_APP', '0015_alter_controle_moto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controle',
            name='moto',
        ),
    ]
