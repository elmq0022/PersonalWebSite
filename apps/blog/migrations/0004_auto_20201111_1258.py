# Generated by Django 3.1.3 on 2020-11-11 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201111_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='date',
            new_name='published',
        ),
    ]
