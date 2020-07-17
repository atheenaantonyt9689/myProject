# Generated by Django 2.1.7 on 2019-12-15 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latestapp', '0013_auto_20191212_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Legalofficer',
            fields=[
                ('userid', models.EmailField(max_length=35, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=35)),
                ('professional_summary', models.CharField(max_length=500)),
                ('core_qualification', models.CharField(max_length=200)),
                ('practice', models.CharField(max_length=30)),
                ('experience', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Medicalofficer',
            fields=[
                ('userid', models.EmailField(max_length=35, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=35)),
                ('professional_summary', models.CharField(max_length=500)),
                ('core_qualification', models.CharField(max_length=200)),
                ('practice', models.CharField(max_length=30)),
                ('experience', models.CharField(max_length=30)),
            ],
        ),
    ]
