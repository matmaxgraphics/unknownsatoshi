# Generated by Django 3.2.9 on 2022-01-04 22:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_alter_subscriptionhistory_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionhistory',
            name='start_date',
            field=models.DateField(default=datetime.date(2022, 1, 4)),
        ),
    ]