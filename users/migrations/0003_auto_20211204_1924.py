# Generated by Django 3.2.9 on 2021-12-05 00:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20211204_1850'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profle',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='create',
            new_name='created',
        ),
    ]
