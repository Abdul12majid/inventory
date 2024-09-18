from django.db import models

# Create your models here.

class NameField(models.CharField):
	def __init__(self, *args, **kwargs):
		super(NameField, self).__init__(*args, **kwargs)

	def get_prep_value(self, value):
		return str(value).lower()

reorder_level_choice = (
	(5, 5),
	(4, 4),
	(3, 3),
	(2, 2),
	(1, 1),
	)

class Categorie(models.Model):
	name=models.CharField('Category', max_length=255, null=True, blank=True)

	def __str__(self):
		return f'{self.name}'



class Product(models.Model):
	name=NameField('Name', null=False, blank=True, max_length=255)
	qps=models.IntegerField(default='1', null=False, blank=True)
	stock=models.IntegerField(default='0', null=False, blank=True)
	issue_stock=models.IntegerField(default='0', null=False, blank=True)
	total_stock_sold=models.IntegerField(default='0', null=False, blank=True)
	quantity=models.IntegerField('total quantity', default='0', null=False, blank=True)
	issue_quantity=models.IntegerField(default='0', null=True, blank=True)
	total_quantity_sold=models.IntegerField(default='0', null=False, blank=True)
	receive_quantity=models.IntegerField(default='0', null=True, blank=True)
	receive_by=models.CharField(max_length=50, null=True, blank=True)
	r_quantity= models.IntegerField('receipt quantity', default='0', null=False, blank=True)
	r_price=models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
	issue_by=models.CharField(max_length=50, null=True, blank=True)
	
	phone_number=models.CharField(max_length=50, null=True, blank=True)
	created_by=models.CharField(max_length=50, null=True, blank=True)
	reorder_level=models.IntegerField(default='2', null=True, blank=True, choices=reorder_level_choice)
	last_updated=models.DateTimeField(auto_now_add=False, auto_now=True)
	price=models.DecimalField(decimal_places=2, max_digits=10, null=False, blank=True)
	total_price=models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
	export_to_csv=models.BooleanField(default='False')
	category=models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)


	def __str__(self):
		return f'{self.name}'
