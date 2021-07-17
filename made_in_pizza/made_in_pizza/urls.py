from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from pizza_shop.views import show_main_page, show_about_page, show_shopping_cart, show_product_details, add_to_cart, \
    delete_cart, order_create, MyOrderView, AdminOrderView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_main_page, name='main_page'),
    path('about/', show_about_page),
    path('cart/', show_shopping_cart),
    path('product_details/<int:id>', show_product_details),
    path('cart/add/<int:id>', add_to_cart),
    path('cart/delete', delete_cart),
    path('order/create/', order_create),
    path('order/list', MyOrderView.as_view()),
    path('order/status', AdminOrderView.as_view())
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
