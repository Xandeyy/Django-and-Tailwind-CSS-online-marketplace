# Generated by Django 3.2.18 on 2023-09-28 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0004_auto_20230928_2201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationmessage',
            old_name='has_unread',
            new_name='has_unread_messages',
        ),
    ]
