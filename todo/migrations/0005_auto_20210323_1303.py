# Generated by Django 3.1.7 on 2021-03-23 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20210323_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(blank=True, choices=[('programming', 'Programming'), ('bugfix', 'Bugfix'), ('something', 'Something')], max_length=120),
        ),
    ]
