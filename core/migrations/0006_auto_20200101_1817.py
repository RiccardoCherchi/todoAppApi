# Generated by Django 3.0.1 on 2020-01-01 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200101_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
