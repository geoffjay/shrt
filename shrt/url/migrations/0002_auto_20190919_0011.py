# Generated by Django 2.2.5 on 2019-09-19 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='tag',
            field=models.CharField(max_length=4),
        ),
    ]
