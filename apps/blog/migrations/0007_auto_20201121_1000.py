# Generated by Django 3.1.3 on 2020-11-21 16:00

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201113_0336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['tag'],
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_date']},
        ),
        migrations.AlterModelManagers(
            name='article',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
