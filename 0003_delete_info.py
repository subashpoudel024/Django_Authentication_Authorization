# Generated by Django 4.0.3 on 2022-11-08 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_info_delete_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Info',
        ),
    ]