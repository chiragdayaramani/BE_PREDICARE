# Generated by Django 3.0.3 on 2022-11-07 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200118_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='rating',
        ),
    ]
