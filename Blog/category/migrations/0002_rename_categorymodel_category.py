# Generated by Django 4.1.2 on 2022-11-15 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CategoryModel',
            new_name='Category',
        ),
    ]
