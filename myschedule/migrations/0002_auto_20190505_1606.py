# Generated by Django 2.1.7 on 2019-05-05 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myschedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Schedule',
        ),
    ]
