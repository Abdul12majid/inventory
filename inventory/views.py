from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddStockForm, ProductSearchForm, SellForm, SellFormStock
from django import forms

from .models import Product, Categorie

# Create your views here.
def home(request):
	
	return render(request, 'home.html', {})

def contact(request):
	if request.method=="POST":
		your_name=request.POST['your-name']
		your_email=request.POST['your-email']
		message_title=request.POST['title']
		your_message=request.POST['your-message']
		return render(request, 'contact2.html', {'your_name':your_name})
	else:
		return render(request, 'contact2.html', {})


def list_products(request):	
	form=ProductSearchForm(request.POST or None)
	all_products=Product.objects.all()
	if request.method=='POST':
		x = form['name'].value().lower()
		all_products=Product.objects.filter(name__icontains=x)
		category=form['category'].value()
		if (category != ''):
			all_products=Product.objects.filter(category_id=category)
		
	return render(request, 'all_product.html', {'all_products':all_products, 'form':form})

def add_product(request):
	form=AddStockForm()
	if request.method=='POST':
		form=AddStockForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			x=name.lower()
			
			product=Product.objects.filter(name=x).first()
			if not product:
				form.save()
				return redirect('/all_products')
			else:
				messages.success(request, ('Item already exists in store.'))

	return render(request, 'add_product.html', {'form':form})

def update_product(request, product_id):
	product=Product.objects.get(pk=product_id)
	form=AddStockForm(request.POST or None, instance=product)
	if form.is_valid():
		form.save()
		return redirect('/all_products')

	return render(request, 'update_product.html', {'form':form, 'product':product})

def show_product(request, product_id):
	product=Product.objects.get(pk=product_id)
	return render(request, 'show_product.html', {'product':product})


def sell_product(request, product_id):
	queryset=Product.objects.get(pk=product_id)
	form=SellForm(request.POST or None, instance=queryset)
	if form.is_valid():
		data=form.cleaned_data['issue_quantity']
		instance=form.save(commit=False)
		if int(data) > instance.quantity:
			messages.success(request, ('Error selling item !!!'))
		else:
			
			instance.quantity -= int(data)
			instance.total_quantity_sold+=int(data)
			instance.total_price=instance.quantity*instance.price
			price_sold=instance.price*int(data)
			instance.stock=instance.quantity/instance.qps
			messages.success(request, (f'{data} {instance.name} sold for {price_sold}'))
			instance.save()
			return redirect('/all_products')
	return render(request, 'sell_product.html', {'form':form})


def sell_product_stock(request, stock_id):
	queryset=Product.objects.get(pk=stock_id)
	form=SellFormStock(request.POST or None, instance=queryset)
	if form.is_valid():
		data=form.cleaned_data['issue_stock']
		instance=form.save(commit=False)
		if int(data) > instance.stock:
			messages.success(request, ('Error selling item !!!'))
		else:
			instance.stock-= int(data)
			instance.total_stock_sold += int(data)
			instance.quantity=instance.quantity-instance.qps
			price_sold=instance.price*instance.qps
			instance.total_price=instance.quantity*instance.price
			messages.success(request, (f'{data} stock of {instance.name} sold for {price_sold}'))

			instance.save()
			return redirect('/all_products')
	return render(request, 'sell_product_stock.html', {'form':form})












