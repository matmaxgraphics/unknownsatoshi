# Generated by Django 3.2.4 on 2022-10-28 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0037_auto_20221025_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cms',
            name='tp_achieved',
            field=models.TextField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='subscriptionhistory',
            name='start_date',
            field=models.DateField(default=datetime.date(2022, 10, 28)),
        ),
    ]