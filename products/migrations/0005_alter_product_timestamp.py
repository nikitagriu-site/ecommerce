# Generated by Django 3.2 on 2021-05-06 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 11, 27, 5, 556615)),
        ),
    ]
