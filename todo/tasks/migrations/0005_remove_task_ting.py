# Generated by Django 3.0.5 on 2020-04-07 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_ting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='ting',
        ),
    ]
