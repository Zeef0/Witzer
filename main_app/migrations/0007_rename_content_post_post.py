# Generated by Django 4.0.4 on 2022-04-23 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_witzuser_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='post',
        ),
    ]
