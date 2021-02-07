# Generated by Django 3.1.5 on 2021-02-04 11:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes27Jan',
            fields=[
                ('title', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=200)),
                ('comment', models.CharField(default='', max_length=200)),
                ('comment1', models.CharField(default='', max_length=200)),
                ('comment2', models.CharField(default='', max_length=200)),
                ('comment3', models.CharField(default='', max_length=200)),
                ('comment4', models.CharField(default='', max_length=200)),
                ('keywords', models.CharField(default='', max_length=200)),
                ('id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('What', models.CharField(default='', max_length=70)),
                ('Why', models.CharField(default='', max_length=70)),
                ('When', models.CharField(default='', max_length=70)),
                ('Who', models.CharField(default='', max_length=70)),
                ('Where', models.CharField(default='', max_length=70)),
                ('keywords', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=200)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]
