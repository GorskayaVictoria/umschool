# Generated by Django 3.0.6 on 2020-05-16 11:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200516_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm_code',
            field=models.UUIDField(default=uuid.UUID('0e8af0a2-6b65-4793-a724-57a4899a7f66')),
        ),
    ]
