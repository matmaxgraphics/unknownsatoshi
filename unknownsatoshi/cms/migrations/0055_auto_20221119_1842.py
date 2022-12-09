# Generated by Django 3.2.9 on 2022-11-19 18:42

import cms.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0054_auto_20221119_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firsttimeplan',
            name='title',
            field=models.CharField(choices=[('weekly plan', 'weekly plan'), ('monthly plan', 'monthly plan'), ('quarterly plan', 'quarterly plan'), ('half a year plan', 'half a year plan')], max_length=90, validators=[cms.models.validate_existing_plan]),
        ),
        migrations.AlterField(
            model_name='plan',
            name='title',
            field=models.CharField(choices=[('weekly plan', 'weekly plan'), ('monthly plan', 'monthly plan'), ('quarterly plan', 'quarterly plan'), ('half a year plan', 'half a year plan')], max_length=90, validators=[cms.models.validate_existing_plan]),
        ),
    ]
