# Generated by Django 3.2.6 on 2021-10-08 10:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_coments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coments',
            options={'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
