# Generated by Django 4.2 on 2023-04-22 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='benchmark',
            name='error',
            field=models.BooleanField(default=False),
        ),
    ]
