# Generated by Django 3.1.6 on 2021-02-12 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodjournal', '0041_auto_20210212_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodjournal',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foodjournal.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
