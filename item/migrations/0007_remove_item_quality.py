# Generated by Django 3.2.18 on 2023-10-08 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_alter_item_quality'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quality',
        ),
    ]
