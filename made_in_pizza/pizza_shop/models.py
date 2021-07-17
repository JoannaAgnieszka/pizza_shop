from django.db import models


class Product(models.Model):
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()
    ingredients = models.ManyToManyField('Ingredient', blank=True, null=True)
    regular_price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Pizza(Product):
    SIZE_CHOICES = {
        (1, 'big'),
        (2, 'small'),
    }
    size = models.IntegerField(max_length=64,
                               choices=SIZE_CHOICES),
    big_price = models.DecimalField(max_digits=6, decimal_places=2)


class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.name


class ProductQuantity(models.Model):
    order = models.ForeignKey('Order', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    ingredient = models.ManyToManyField(Ingredient, through='IngredientQuantity')


class IngredientQuantity(models.Model):
    product = models.ForeignKey(ProductQuantity, on_delete=models.PROTECT)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.IntegerField()


class Order(models.Model):
    PICKUP_METHOD = (
        (1, 'Dowóz'),
        (2, 'Odbiór własny'),
        (2, 'Zjem na miejscu'),
    )

    DELIVERY_POINT = (
        (1, 'Wejście na plażę nr 1'),
        (2, 'Wejście na plażę nr 2'),
        (3, 'Wejście na plażę nr 3'),
        (4, 'Wejście na plażę nr 4'),
        (5, 'Wejście na plażę nr 5'),
        (6, 'Wejście na plażę nr 6'),
        (7, 'Pod wskazany adres'),
    )

    PAYMENT_METHOD = (
        (1, 'Gotówka'),
        (2, 'Blik'),
        (3, 'Karta'),
    )

    STATUS = (
        (1, 'Received'),
        (2, 'In progress'),
        (3, 'Delivered'),
    )

    def __str__(self):
        return f'{self.pk} {self.phone_number} {self.client_name} {self.get_status_display()}'

    product = models.ManyToManyField(Product, through=ProductQuantity)
    total_sum = models.DecimalField(max_digits=6, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)
    pickup_method = models.IntegerField(choices=PICKUP_METHOD, verbose_name='Rodzaj odbioru')
    delivery_point = models.IntegerField(choices=DELIVERY_POINT, verbose_name='Punkt dostawy')
    payment_method = models.IntegerField(choices=PAYMENT_METHOD, verbose_name='Sposób płatności')
    client_name = models.CharField(max_length=64, verbose_name='Imię')
    phone_number = models.CharField(max_length=64, verbose_name='Telefon')
    city = models.CharField(max_length=64, blank=True, null=True, verbose_name='Miejscowość')
    postal_code = models.CharField(max_length=64, blank=True, null=True, verbose_name='Kod pocztowy')
    street = models.CharField(max_length=64, blank=True, null=True, verbose_name='Ulica')
    house_nr = models.CharField(max_length=64, blank=True, null=True, verbose_name='Nr')
    comment = models.TextField(blank=True, null=True, verbose_name='Komentarz')
    status = models.IntegerField(choices=STATUS)



