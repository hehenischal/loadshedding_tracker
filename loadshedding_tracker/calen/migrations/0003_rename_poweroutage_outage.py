# Generated by Django 4.2.2 on 2023-08-04 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calen', '0002_remove_poweroutage_ward_poweroutage_ward_number_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PowerOutage',
            new_name='Outage',
        ),
    ]