# Generated by Django 3.2.2 on 2021-05-15 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_product_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 15, 19, 51, 6, 332424)),
        ),
    ]
