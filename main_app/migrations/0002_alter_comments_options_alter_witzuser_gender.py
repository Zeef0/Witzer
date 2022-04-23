# Generated by Django 4.0.4 on 2022-04-21 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'comments'},
        ),
        migrations.AlterField(
            model_name='witzuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Other', 'Other')], default=' ', max_length=50),
        ),
    ]
