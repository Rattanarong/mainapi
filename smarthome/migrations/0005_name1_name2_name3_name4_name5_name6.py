# Generated by Django 3.2 on 2022-02-28 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarthome', '0004_auto_20220215_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='name1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swname1', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='name2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swname2', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='name3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swname3', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='name4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swname4', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='name5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swname5', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='name6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swname6', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
