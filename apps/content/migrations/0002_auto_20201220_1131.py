# Generated by Django 3.1.4 on 2020-12-20 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'About', 'verbose_name_plural': 'About'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': 'Projects', 'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterModelOptions(
            name='resume',
            options={'verbose_name': 'Resume', 'verbose_name_plural': 'Resume'},
        ),
    ]
