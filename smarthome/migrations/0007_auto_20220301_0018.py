# Generated by Django 3.2 on 2022-02-28 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smarthome', '0006_auto_20220301_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device1',
            name='namesw1',
        ),
        migrations.RemoveField(
            model_name='device2',
            name='namesw21',
        ),
        migrations.RemoveField(
            model_name='device2',
            name='namesw22',
        ),
        migrations.RemoveField(
            model_name='device3',
            name='namesw31',
        ),
        migrations.RemoveField(
            model_name='device3',
            name='namesw32',
        ),
        migrations.RemoveField(
            model_name='device3',
            name='namesw33',
        ),
    ]
