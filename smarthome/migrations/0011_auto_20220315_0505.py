# Generated by Django 3.2 on 2022-03-14 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smarthome', '0010_auto_20220304_0242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device1',
            name='stsw1',
        ),
        migrations.RemoveField(
            model_name='device2',
            name='stsw21',
        ),
        migrations.RemoveField(
            model_name='device2',
            name='stsw22',
        ),
        migrations.RemoveField(
            model_name='device3',
            name='stsw31',
        ),
        migrations.RemoveField(
            model_name='device3',
            name='stsw32',
        ),
        migrations.RemoveField(
            model_name='device3',
            name='stsw33',
        ),
    ]
