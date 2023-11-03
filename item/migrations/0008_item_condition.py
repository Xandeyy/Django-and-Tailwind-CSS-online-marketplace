# Generated by Django 3.2.18 on 2023-10-08 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_remove_item_quality'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='condition',
            field=models.CharField(choices=[('new', 'New'), ('used', 'Used')], default='new', max_length=10),
        ),
    ]
