# Generated by Django 4.0.5 on 2022-07-09 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_people'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={'managed': False, 'ordering': ['name']},
        ),
    ]
