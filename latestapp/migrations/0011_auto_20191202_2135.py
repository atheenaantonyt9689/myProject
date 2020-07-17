# Generated by Django 2.1.7 on 2019-12-02 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latestapp', '0010_auto_20191202_1359'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Log',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='contact_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='userid',
            field=models.EmailField(max_length=35, primary_key=True, serialize=False),
        ),
    ]
