from django.contrib import admin
from pizza_shop.models import Ingredient, Product, Type, Pizza


class AdminPizza(admin.ModelAdmin):
    list_display = ['name', 'type', 'description', 'regular_price', 'big_price']
    search_fields = ['name']


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'type', 'description', 'regular_price']
    search_fields = ['name']


class AdminIngredient(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']


admin.site.register(Ingredient, AdminIngredient)
admin.site.register(Product, AdminProduct)
admin.site.register(Pizza, AdminPizza)
admin.site.register(Type)
