# Generated by Django 4.2.2 on 2023-10-20 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PLAQUES_APP', '0014_alter_controle_moto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controle',
            name='moto',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
