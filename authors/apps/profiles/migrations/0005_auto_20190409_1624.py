# Generated by Django 2.1.7 on 2019-04-09 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20190409_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='followers',
            new_name='followers_no',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='following',
            new_name='following_no',
        ),
    ]