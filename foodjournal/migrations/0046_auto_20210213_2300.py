# Generated by Django 3.1.6 on 2021-02-13 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodjournal', '0045_auto_20210213_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rec_bmr',
            field=models.IntegerField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='rec_cal_lose',
            field=models.IntegerField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='rec_calories',
            field=models.IntegerField(default=True),
            preserve_default=False,
        ),
    ]
