# Generated by Django 3.1.3 on 2020-12-01 21:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20201126_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='next_review_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 1, 21, 43, 46, 805599, tzinfo=utc)),
        ),
    ]
