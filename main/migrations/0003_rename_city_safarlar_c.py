# Generated by Django 3.2.9 on 2022-03-28 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_videonews_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='safarlar',
            old_name='city',
            new_name='c',
        ),
    ]
