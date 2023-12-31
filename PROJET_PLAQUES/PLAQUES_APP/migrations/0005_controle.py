# Generated by Django 4.2.2 on 2023-10-18 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PLAQUES_APP', '0004_delete_controle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Controle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moto', models.CharField(max_length=100, unique=True)),
                ('Num_Plaque', models.CharField(max_length=50, unique=True)),
                ('Proprietaire', models.CharField(max_length=100, unique=True)),
                ('Photo_proprietaire', models.ImageField(blank=True, upload_to='photoapp')),
                ('Exonerations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PLAQUES_APP.exoneration')),
                ('enregistrement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PLAQUES_APP.enregistrement')),
            ],
            options={
                'verbose_name': 'Controle',
                'verbose_name_plural': 'Controle',
            },
        ),
    ]
