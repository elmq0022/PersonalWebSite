# Generated by Django 3.1.5 on 2021-01-27 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210124_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='name',
        ),
    ]
