# Generated by Django 4.2.2 on 2023-10-20 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PLAQUES_APP', '0009_delete_controle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Controle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moto', models.CharField(max_length=60)),
                ('Proprietaire', models.CharField(max_length=100)),
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
