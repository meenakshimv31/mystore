# Generated by Django 4.1 on 2022-08-23 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobiles',
            name='is_active',
        ),
    ]
