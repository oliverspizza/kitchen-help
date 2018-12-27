# Generated by Django 2.1.2 on 2018-12-27 03:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliablity',
            name='not_available',
            field=models.DateField(default=None, help_text='Date format must be typed like so: 2018-12-25'),
        ),
        migrations.AlterField(
            model_name='avaliablity',
            name='person',
            field=models.ForeignKey(default=None, help_text='Make sure you select your name.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]