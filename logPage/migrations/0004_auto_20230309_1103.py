# Generated by Django 3.2.18 on 2023-03-09 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logPage', '0003_login_signup'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='signup',
            new_name='User',
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]
