# Generated by Django 3.2.6 on 2021-10-12 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='tiltle',
            new_name='title',
        ),
    ]