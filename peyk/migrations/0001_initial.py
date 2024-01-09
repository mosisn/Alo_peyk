# Generated by Django 5.0 on 2024-01-09 07:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Tehran')),
                ('address', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Tehran')),
                ('address', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('No', models.CharField(max_length=5)),
                ('destination', models.ManyToManyField(to='peyk.destination')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='peyk.origin')),
            ],
        ),
        migrations.AddField(
            model_name='destination',
            name='origin',
            field=models.ManyToManyField(to='peyk.origin'),
        ),
    ]
