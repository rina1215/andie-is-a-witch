# Generated by Django 3.1.4 on 2020-12-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201229_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='collection',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]