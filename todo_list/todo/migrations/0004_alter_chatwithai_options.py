# Generated by Django 4.2.17 on 2025-04-16 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_rename_chat_chatwithai'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatwithai',
            options={'ordering': ['created_at'], 'verbose_name': 'Chat with AI', 'verbose_name_plural': 'Chats with AI'},
        ),
    ]
