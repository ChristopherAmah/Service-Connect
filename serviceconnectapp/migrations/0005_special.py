# Generated by Django 5.0.3 on 2024-03-12 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceconnectapp', '0004_service_special'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='specials/')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Special',
                'verbose_name_plural': 'Specials',
                'db_table': 'specials',
                'managed': True,
            },
        ),
    ]
