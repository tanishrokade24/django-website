# Generated by Django 3.0.5 on 2020-12-19 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='post',
            new_name='blog',
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='author_name',
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='img',
        ),
    ]
