# Generated by Django 3.1.7 on 2021-03-24 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_remove_task_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finished_at',
            field=models.DateTimeField(null=True),
        ),
    ]
