from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView

from pizza_shop.forms import OrderForm
from pizza_shop.models import Type, Product, Ingredient, ProductQuantity, Order, IngredientQuantity


def show_main_page(request):
    types = Type.objects.all()
    return render(request, 'main_page.html', {'types': types})


def show_about_page(request):
    return render(request, 'about.html')


def show_product_details(request, id):
    product = Product.objects.get(pk=id)
    ingredients = Ingredient.objects.all()
    return render(request, 'product_details.html', {'product': product, 'ingredients': ingredients})


def fetch_product_from_cart(request):
    cart = request.session.get('cart')
    total_sum = 0
    product_list = []
    if cart is not None:
        for id, quantity in cart:
            product = Product.objects.get(pk=id)
            product_list.append((product, quantity))
            product.part_sum = product.regular_price * quantity
            total_sum += product.part_sum
    return product_list, total_sum


def fetch_product_and_ingredients_from_cart(request):
    cart = request.session.get('cart')
    total_sum = 0
    product_list = []  # za chwile w petli iterujacej po produkcie utworzymy pustą listę skladnikow,
    # ktora będzie nam sie czyścić po każdym dodaniu skladnikow do kolejnego produktu,
    # żeby przed dodaniem skladnikow do nastepnego produktu, byla pusta,
    # czyli nie powielala dodanych skaldnikow z produktu poprzedniego
    if cart is not None:
        for id, quantity, ingredients, user_price in cart:
            ingredient_list = []
            product = Product.objects.get(pk=id)
            product.regular_price = user_price
            # product_list.append((product, quantity)) #przeniesiemy to poza petle or poniewaz jest za wysoko,
            # jeszcze program nie wie nic o skladnikach
            product.part_sum = product.regular_price * quantity
            total_sum += product.part_sum
            for ingredient_id, ingredient_quantity in ingredients:
                ingredient = Ingredient.objects.get(pk=ingredient_id)
                ingredient_list.append((ingredient, ingredient_quantity))

            product_list.append(
                (product, quantity, ingredient_list))  # to jest krok, w którym odczytanie produktu i skladnków,
            # ktore sa w koszyku, one sa w tej chwili przygotowane do bazy danych,
            # na razie musimy sprawdzic, czy ta funkcja nam dziala i robimy printa
            print('Skladniki produktu')
            print(product, ingredient_list)  # ta funkcja sie wywola przy skladaniu zamowienia

    return product_list, total_sum


# def count_ingredients(ingredients):
#     result = 0
#     for id, quantity in ingredients:
#         ingredient = Ingredient.objects.get(pk=id)
#         result += ingredient.price * int(quantity)
#     return result


def show_shopping_cart(request):
    form = OrderForm()
    product_list, total_sum = fetch_product_and_ingredients_from_cart(request)
    return render(request, 'shopping_cart.html', {'product_list': product_list, 'total_sum': total_sum, 'form': form})


def add_to_cart(request, id):
    if request.method == 'POST':
        user_price = int(request.POST.get('user_price').strip().replace('.00', ''))
        quantity = int(request.POST.get('quantity'))
        ingredient_quantity = request.POST.getlist('ingredientQuantity')
        ingredients = request.POST.getlist('ingredient')
        ingredients_zip = zip(ingredients,
                              ingredient_quantity)  # zip jest generatorem, ktory dopiero w momencie wywolania daje nam wyniki

        # for q, i in data:
        #     result.write(f"id składnika: {i}, ilość: {q} \n <br>")

        if request.session.get('cart') is None:
            request.session['cart'] = []

        request.session['cart'].append((id, quantity, list(ingredients_zip),
                                        user_price))  # dodanie krotki kilkuelementowej, dlaczego w jednym appendzie? chodzi o spójnosc danych,
        # jest to fragment danych, 4 elementy, ktore sie zawsze powtarzaja.
        # Gdyby to byl append dla ingredient i append dla product to wtedy nie wiadomo by bylo, co odczytujemy

        request.session.modified = True
        return redirect('/')


def delete_cart(request):
    if request.session.get('cart') is not None:
        del request.session['cart']
    return redirect('/')


def order_create(request):
    if request.method == 'POST':

        form = OrderForm(request.POST)
        if form.is_valid():

            if request.session.get('cart') is not None:
                product_list, total_sum = fetch_product_and_ingredients_from_cart(request)
                order = form.save(commit=False)
                order.total_sum = total_sum
                order.status = 1
                order.save()
                if request.session.get('order') is None:
                    request.session['order'] = []
                request.session.get('order').append(order.pk)

                for product, quantity, ingredients in product_list:
                    product_qty = ProductQuantity.objects.create(product=product, quantity=quantity, order=order)

                    for ingredient, ingredient_qty in ingredients:
                        IngredientQuantity.objects.create(product=product_qty, ingredient=ingredient,
                                                          quantity=ingredient_qty)

                del request.session['cart']

        else:
            return render(request, 'shopping_cart.html', {'form': form})

        return redirect(reverse_lazy('main_page'))


class MyOrderView(View):
    def get(self, request):
        order = request.session.get('order')
        if order is not None:
            order_list = []
            for id in order:
                order_details = Order.objects.get(pk=id)
                order_list.append(order_details)
            return render(request, 'order_list.html', {'order_list': order_list})
        return render(request, 'order_list.html')


class AdminOrderView(PermissionRequiredMixin, ListView):
    model = Order
    template_name = 'admin_order_status.html'
    fields = '__all__'
    permission_required = 'pizza_shop.view_order'
