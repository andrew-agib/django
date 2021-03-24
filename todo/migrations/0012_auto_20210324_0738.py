# Generated by Django 3.1.7 on 2021-03-24 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0011_auto_20210324_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='finished_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
