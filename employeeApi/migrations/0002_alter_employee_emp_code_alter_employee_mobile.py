# Generated by Django 4.2.5 on 2023-09-15 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_code',
            field=models.CharField(max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
