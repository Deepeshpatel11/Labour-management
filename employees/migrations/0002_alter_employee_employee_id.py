# Generated by Django 5.1.5 on 2025-02-03 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(help_text='Unique Employee ID', max_length=18, unique=True),
        ),
    ]
