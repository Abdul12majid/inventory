from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import AddStockForm, ProductSearchForm, SellForm, SellFormStock, RegisterUserForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Product, Categorie
from django.contrib.auth.forms import UserCreationForm

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
			messages.success(request, (f'Quantity of {instance.name} not up to that, available quantity = {instance.quantity} !!!'))
		else:
			if instance.quantity <= 1:
				messages.success(request, ('Too low, kindly update product.'))
			else:
				instance.quantity -= int(data)
				instance.total_quantity_sold+=int(data)
				instance.total_price=instance.quantity*instance.price
				price_sold=instance.price*int(data)
				instance.issue_by=request.user.username
				instance.r_quantity = int(data)
				instance.r_price = price_sold
				if instance.qps != 0:
					instance.stock=instance.quantity/instance.qps
				messages.success(request, (f'{data} {instance.name} sold for {price_sold}'))
				instance.save()
				instance.r_price=0
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
			messages.success(request, (f'Stock of {instance.name} not up to that, available quantity = {instance.stock} !!!'))
		else:
			if instance.stock <= 1:
				messages.success(request, ('Stock is too low, kindly update. '))
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



def history(request):
	total_history = Product.objects.all()
	return render(request, 'history.html', {'total_history':total_history})


def login_user(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('Login Successful'))
			return redirect('all-products')
		else:
			messages.success(request, ("Error Logging In"))
			return HttpResponseRedirect('/')
	else:
		return render(request, "home.html", {})


def register_user(request):
	if request.method=='POST':
		form=RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data['username']
			password=form.cleaned_data['password1']
			user=authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Account Created Successfully"))
			return HttpResponseRedirect('/')
		else:
			messages.success(request, ('Error with details provided'))
			return redirect('register-user')
	else:
		form=RegisterUserForm()
	return render(request, 'register.html', {'form':form})

def logout_user(request):
	if request.user.is_authenticated:
		logout(request)
		messages.success(request, ('You have been logged out.'))
		return HttpResponseRedirect('/login_user')
		
	else:
		messages.success(request, ("You're logged out already"))
		return render(request, "login.html", {})

def receipt(request):
	all_receipt=Product.objects.all()
	return render(request, 'receipt.html', {'all_receipt':all_receipt})


