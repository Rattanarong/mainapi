# Generated by Django 3.2 on 2022-03-03 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarthome', '0009_auto_20220304_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='device1',
            name='stsw1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='device2',
            name='stsw21',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='device2',
            name='stsw22',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='device3',
            name='stsw31',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='device3',
            name='stsw32',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='device3',
            name='stsw33',
            field=models.TextField(blank=True, null=True),
        ),
    ]
