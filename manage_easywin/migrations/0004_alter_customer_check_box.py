# Generated by Django 4.2.8 on 2024-01-14 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_easywin', '0003_customer_check_box'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='check_box',
            field=models.CharField(default='unchecked', max_length=10),
        ),
    ]
