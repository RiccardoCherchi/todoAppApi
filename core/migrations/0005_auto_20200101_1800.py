# Generated by Django 3.0.1 on 2020-01-01 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200101_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo', to='core.List'),
        ),
    ]
