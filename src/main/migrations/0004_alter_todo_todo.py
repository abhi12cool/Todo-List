# Generated by Django 3.2.7 on 2021-11-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_todo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo',
            field=models.CharField(max_length=500),
        ),
    ]