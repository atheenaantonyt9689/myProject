# Generated by Django 2.1.7 on 2019-11-29 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latestapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('usertype', models.CharField(max_length=20)),
            ],
        ),
    ]