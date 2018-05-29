# Generated by Django 2.0.5 on 2018-05-28 23:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call_log', '0006_auto_20180528_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 28, 20, 56, 30, 855941)),
        ),
        migrations.AlterField(
            model_name='callrecord',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
    ]