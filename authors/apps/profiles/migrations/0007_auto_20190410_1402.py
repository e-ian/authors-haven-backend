# Generated by Django 2.1.7 on 2019-04-10 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20190409_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followers_no',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='following_no',
        ),
    ]