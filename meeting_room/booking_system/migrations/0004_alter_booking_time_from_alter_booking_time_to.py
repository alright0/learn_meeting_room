# Generated by Django 4.1.2 on 2022-11-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0003_alter_booking_time_from_alter_booking_time_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time_from',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time_to',
            field=models.TimeField(default='00:00'),
        ),
    ]
