# Generated by Django 3.0.6 on 2020-05-16 11:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200516_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm_code',
            field=models.UUIDField(default=uuid.UUID('bb9900ae-3ea8-4a8e-9102-91eccf2f31d9')),
        ),
    ]
