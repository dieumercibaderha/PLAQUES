# Generated by Django 4.2.2 on 2023-10-20 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PLAQUES_APP', '0016_remove_controle_moto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='controle',
            old_name='enregistrement',
            new_name='Num_Plaque',
        ),
        migrations.RemoveField(
            model_name='controle',
            name='Photo_proprietaire',
        ),
        migrations.RemoveField(
            model_name='controle',
            name='Proprietaire',
        ),
    ]
