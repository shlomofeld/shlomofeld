# Generated by Django 3.0.5 on 2020-04-07 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_remove_task_additional_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='ting',
            field=models.CharField(default='hi', max_length=500),
            preserve_default=False,
        ),
    ]
