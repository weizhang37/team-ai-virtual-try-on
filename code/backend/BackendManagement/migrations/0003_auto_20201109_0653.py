# Generated by Django 3.1.2 on 2020-11-09 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BackendManagement', '0002_auto_20201109_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='owned_saler',
            field=models.ForeignKey(limit_choices_to={'is_saler': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
