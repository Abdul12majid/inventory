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
    path('history', views.history, name='history'),
    path('register_user', views.register_user, name="register-user"),
    path('login_user', views.login_user, name="login-user"),
    path('logout_user', views.logout_user, name="logout-user"),
    path('print_receipt', views.receipt, name="print-receipt"),
]
