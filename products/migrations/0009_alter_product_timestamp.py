# Generated by Django 3.2.2 on 2021-05-15 07:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 15, 10, 55, 33, 170775)),
        ),
    ]
