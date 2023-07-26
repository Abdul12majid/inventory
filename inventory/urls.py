from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('add_product', views.add_product, name='add-product'),
    path('update_product/<product_id>', views.update_product, name='update-product'),
    path('sell_product/<product_id>', views.sell_product, name='sell-product'),
    path('sell_product_stock/<stock_id>', views.sell_product_stock, name='sell-product-stock'),
    path('show_product/<product_id>', views.show_product, name='show-product'),
    path('all_products', views.list_products, name='all-products'),
    path('contact', views.contact, name='contact'),
]
