# Generated by Django 4.1.7 on 2023-03-23 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_piec_word_words_word_2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='words',
            old_name='word_2',
            new_name='real_word',
        ),
    ]
