# Generated by Django 3.2 on 2021-06-23 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_shop', '0010_auto_20210619_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Received'), (2, 'In progress'), (3, 'Delivered')], default=1),
            preserve_default=False,
        ),
    ]
