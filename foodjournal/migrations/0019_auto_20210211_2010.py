# Generated by Django 3.1.6 on 2021-02-11 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodjournal', '0018_auto_20210211_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodjournal',
            name='date',
            field=models.DateField(),
        ),
    ]
