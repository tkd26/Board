# Generated by Django 3.1.3 on 2020-11-19 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0005_auto_20201118_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='goodtext',
            field=models.CharField(blank=True, default='a ', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='readtext',
            field=models.CharField(blank=True, default='a ', max_length=200, null=True),
        ),
    ]