# Generated by Django 5.0.3 on 2024-03-12 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviceconnectapp', '0005_special'),
    ]

    operations = [
        migrations.RenameField(
            model_name='special',
            old_name='image',
            new_name='spec_image',
        ),
        migrations.RemoveField(
            model_name='special',
            name='description',
        ),
        migrations.RemoveField(
            model_name='special',
            name='name',
        ),
    ]
