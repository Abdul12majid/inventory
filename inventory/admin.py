from django.contrib import admin
from .models import Product, Categorie
from .forms import AddStockForm

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display=('name', 'stock', 'quantity', 'price', 'category', 'total_quantity_sold', 'total_stock_sold', 'qps', 'total_price',)
	list_filter=('category', 'name',)
	form=AddStockForm
	search_fields=('name',)


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
	pass