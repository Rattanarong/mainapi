# Generated by Django 3.2 on 2022-03-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarthome', '0007_auto_20220301_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='device1',
            name='namesw1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='device2',
            name='namesw21',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='device2',
            name='namesw22',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='device3',
            name='namesw31',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='device3',
            name='namesw32',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='device3',
            name='namesw33',
            field=models.TextField(blank=True, null=True),
        ),
    ]
