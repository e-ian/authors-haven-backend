# Generated by Django 2.1.7 on 2019-04-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20190409_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='followers_no',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='following_no',
            field=models.PositiveIntegerField(default=0),
        ),
    ]