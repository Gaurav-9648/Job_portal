# Generated by Django 3.1.3 on 2023-05-23 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_auto_20230522_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruiter',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='recruiter',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='last_name',
        ),
    ]
