# Generated by Django 3.2.2 on 2021-05-19 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(default='Moldova', max_length=100),
        ),
    ]
