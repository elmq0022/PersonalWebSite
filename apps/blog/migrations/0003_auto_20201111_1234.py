# Generated by Django 3.1.3 on 2020-11-11 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_articlemodel_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArticleModel',
            new_name='Article',
        ),
    ]
