# Generated by Django 2.1.2 on 2018-11-10 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_auto_20181109_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10000),
            preserve_default=False,
        ),
    ]
