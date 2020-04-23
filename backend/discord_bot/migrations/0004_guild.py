# Generated by Django 3.0.4 on 2020-04-21 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discord_bot', '0003_auto_20200401_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('connected_channel', models.TextField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
