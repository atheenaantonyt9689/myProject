# Generated by Django 2.1.7 on 2019-12-02 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latestapp', '0009_log_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='password',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
