# Generated by Django 3.2.18 on 2023-10-03 03:10

from django.db import migrations, models
import item.models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_number',
            field=models.CharField(default=item.models.generate_item_number, max_length=8, unique=True),
        ),
    ]
