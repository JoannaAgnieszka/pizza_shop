# Generated by Django 3.2 on 2021-05-14 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_shop', '0006_auto_20210514_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='end_date',
        ),
        migrations.AlterField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
