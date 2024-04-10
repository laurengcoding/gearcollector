# Generated by Django 5.0.4 on 2024-04-10 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=256)),
                ('make', models.CharField(max_length=256)),
                ('type', models.CharField(max_length=256)),
                ('model', models.CharField(max_length=256)),
                ('colour', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Serviced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('serviced', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('g', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.gear')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
