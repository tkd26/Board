# Generated by Django 3.1.3 on 2020-11-21 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0008_customusermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boardapp.customusermodel'),
        ),
    ]
