# Generated by Django 4.1.7 on 2023-03-23 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='course',
            new_name='standard',
        ),
    ]
