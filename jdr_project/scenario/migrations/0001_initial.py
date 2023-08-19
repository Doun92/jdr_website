# Generated by Django 4.2.4 on 2023-08-19 20:33

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scénario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Acte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('numero', models.PositiveSmallIntegerField()),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scenario.scénario')),
            ],
        ),
    ]
