# Generated by Django 3.1.6 on 2021-02-13 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodjournal', '0044_user_activity_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='maleOrFemale',
            new_name='male_or_female',
        ),
    ]
