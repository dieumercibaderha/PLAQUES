# Generated by Django 4.2.2 on 2023-10-20 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PLAQUES_APP', '0013_alter_controle_proprietaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controle',
            name='moto',
            field=models.TextField(max_length=100),
        ),
    ]
