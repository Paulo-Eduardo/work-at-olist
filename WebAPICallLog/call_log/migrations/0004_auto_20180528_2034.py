# Generated by Django 2.0.5 on 2018-05-28 23:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call_log', '0003_auto_20180528_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(blank=True, max_length=20)),
                ('destination', models.CharField(blank=True, max_length=20)),
                ('start_time', models.DateTimeField(blank=True)),
                ('end_time', models.DateTimeField(blank=True)),
                ('duration', models.TimeField(blank=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AlterField(
            model_name='call',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 28, 20, 34, 48, 935013)),
        ),
    ]
