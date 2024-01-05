# Generated by Django 5.0 on 2024-01-05 09:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('No', models.CharField(max_length=4)),
                ('Unit', models.CharField(max_length=3)),
                ('description', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='peyk.city')),
            ],
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('No', models.CharField(max_length=4)),
                ('Unit', models.CharField(max_length=3)),
                ('description', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='peyk.city')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='peyk.destination')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='peyk.origin')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='peyk.province'),
        ),
    ]