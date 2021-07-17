# Generated by Django 3.2 on 2021-05-07 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_shop', '0004_auto_20210506_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_method',
            field=models.IntegerField(choices=[(1, 'Beach_point_1'), (2, 'Beach_point_2'), (3, 'Beach_point_3'), (4, 'Beach_point_4'), (5, 'Beach_point_5'), (6, 'Beach_point_6'), (7, 'delivery to your door')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='pickup_method',
            field=models.IntegerField(choices=[(1, 'delivery'), (2, 'pick-up')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredients',
            field=models.ManyToManyField(blank=True, null=True, to='pizza_shop.Ingredient'),
        ),
    ]