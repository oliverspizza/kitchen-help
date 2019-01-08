# Generated by Django 2.1.2 on 2019-01-08 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_avaliablity_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliablity',
            name='not_available',
            field=models.DateField(default=None, help_text='You can only select one date per submit.'),
        ),
        migrations.AlterField(
            model_name='avaliablity',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
