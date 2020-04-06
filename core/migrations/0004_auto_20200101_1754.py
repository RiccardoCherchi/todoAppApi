# Generated by Django 3.0.1 on 2020-01-01 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='todo',
        ),
        migrations.AddField(
            model_name='todo',
            name='todo_list',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='todo', to='core.List'),
            preserve_default=False,
        ),
    ]
