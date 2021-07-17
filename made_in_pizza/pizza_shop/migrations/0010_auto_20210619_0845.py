# Generated by Django 3.2 on 2021-06-19 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_shop', '0009_auto_20210610_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_point',
            field=models.IntegerField(choices=[(1, 'Wejście na plażę nr 1'), (2, 'Wejście na plażę nr 2'), (3, 'Wejście na plażę nr 3'), (4, 'Wejście na plażę nr 4'), (5, 'Wejście na plażę nr 5'), (6, 'Wejście na plażę nr 6'), (7, 'Pod wskazany adres'), (8, 'Zjem w barze')], verbose_name='Punkt dostawy'),
        ),
        migrations.CreateModel(
            name='IngredientQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pizza_shop.ingredient')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pizza_shop.productquantity')),
            ],
        ),
        migrations.AddField(
            model_name='productquantity',
            name='ingredient',
            field=models.ManyToManyField(through='pizza_shop.IngredientQuantity', to='pizza_shop.Ingredient'),
        ),
    ]
