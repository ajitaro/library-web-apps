# Generated by Django 5.1.1 on 2024-10-04 23:15

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('number', models.IntegerField(
                    primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('release_date', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('pages', models.IntegerField()),
                ('cover', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('borrow_date', models.DateField(
                    default=django.utils.timezone.now)),
                ('return_date', models.DateField()),
                ('book', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.book')),
            ],
        ),
    ]
