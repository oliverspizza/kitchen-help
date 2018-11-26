# Generated by Django 2.1.2 on 2018-11-12 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20181112_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='day_of_week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Day'),
        ),
        migrations.AlterField(
            model_name='prepwork',
            name='day_of_week',
            field=models.CharField(choices=[('Mon', 'Monday'), ('Tues', 'Tuesday'), ('Wed', 'Wednesday'), ('Thur', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], help_text='Please set the day of week. ', max_length=20),
        ),
    ]
