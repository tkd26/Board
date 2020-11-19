# Generated by Django 3.1.3 on 2020-11-18 04:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0004_auto_20201117_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boardmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]