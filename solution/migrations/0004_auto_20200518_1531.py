# Generated by Django 3.0.6 on 2020-05-18 15:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0003_auto_20200518_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
