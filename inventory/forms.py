from django import forms
from django.forms import ModelForm
from .models import Product

class AddStockForm(ModelForm):
	class Meta:
		model=Product
		fields=('name', 'qps', 'quantity', 'stock', 'price', 'category', 'reorder_level', 'issue_quantity',)
		widgets={

		    'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name *', 'type':'text', 'name':'your-name'}),
		    'quantity':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Quantity *', 'type':'number', 'name':'quantity'}),
		    'stock':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Stock *', 'type':'number', 'name':'stock'}),
		    'price':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Price *', 'type':'number', 'name':'price'}),
		    'qps':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'category', 'required':'True', 'name':'category'}),
		    'category':forms.Select(attrs={'class':'form-control', 'placeholder':'category', 'required':'True', 'name':'category'}),
		}
		labels={

		    'name':'Name',
		    'email':'',
		    'phone_number':'',
		    'message':'',

		    }
    
class ProductSearchForm(ModelForm):
	class Meta:
		model=Product
		fields=('name','category',)
		widgets={

		    'name':forms.TextInput(attrs={'class':'form-control border-0 bg-light px-4', 'style':'height:40px;', 'required':'False', 'placeholder':'Item Name *', 'type':'text'}),
        }

class SellForm(ModelForm):
	
	class Meta:
		model=Product
		fields=('issue_quantity',)
		widgets={

		    'issue_quantity':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'How many *', 'type':'number', 'name':'quantity'}),
		    
		    }

class SellFormStock(ModelForm):
	class Meta:
		model=Product
		fields=('issue_stock',)
		widgets={

		    'issue_stock':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'How many *', 'type':'number', 'name':'quantity'}),
		    
		    }