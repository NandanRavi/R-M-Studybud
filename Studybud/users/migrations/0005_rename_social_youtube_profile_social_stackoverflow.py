# Generated by Django 4.0 on 2022-11-11 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_profile_social_website'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_youtube',
            new_name='social_stackoverflow',
        ),
    ]