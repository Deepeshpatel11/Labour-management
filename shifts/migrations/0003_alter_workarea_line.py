# Generated by Django 5.1.5 on 2025-02-03 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0002_workarea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workarea',
            name='line',
            field=models.CharField(choices=[('1', 'Line 1'), ('2', 'Line 2'), ('3', 'Line 3'), ('4', 'Line 4'), ('MOH', 'Manufacturing Overhead (MOH)'), ('Shared', 'Shared Resources')], help_text='Select the production line or work area category', max_length=10),
        ),
    ]
