# Generated by Django 3.1.4 on 2020-12-29 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_collection_comment_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='owner',
            new_name='collection_by',
        ),
    ]
