# Generated by Django 3.2.18 on 2023-03-09 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logPage', '0004_auto_20230309_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='emailId',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]
