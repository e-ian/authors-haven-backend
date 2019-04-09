# Generated by Django 2.1.7 on 2019-04-09 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]