# Generated by Django 5.0.2 on 2024-05-09 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='name',
            new_name='dep_name',
        ),
    ]
