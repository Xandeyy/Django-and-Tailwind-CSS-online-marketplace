# Generated by Django 3.2.18 on 2023-10-08 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='phone_number',
        ),
    ]
