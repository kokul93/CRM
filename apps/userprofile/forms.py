from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *

class companyForms(forms.ModelForm):
    
        name=forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Your name .....'}))
        email=forms.EmailField(required=False,widget= forms.TextInput(attrs={'placeholder':'example@mail.com ...'}))
        phone=forms.CharField(label='Phone')
        address1=forms.CharField(label='Address',
                widget= forms.TextInput(attrs={'placeholder':'1234 Main St'})
        )
        address2=forms.CharField(label='',widget= forms.TextInput(attrs={'placeholder':'Apartment , Studio, or Floor'}))
        city=forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Toronto,New York'}))
        zip_code=forms.CharField(label='Zip')

    



        class Meta:
                model=Company
                fields=('name','email','phone','address1','address2','city','zip_code','created')


class contactForm(forms.ModelForm):
    
        name=forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Your name .....'}))
        email=forms.EmailField(required=False,widget= forms.TextInput(attrs={'placeholder':'example@mail.com ...'}))
        phone=forms.CharField(label='Phone')
        address1=forms.CharField(label='Address',
                widget= forms.TextInput(attrs={'placeholder':'1234 Main St'})
        )
        address2=forms.CharField(label='',widget= forms.TextInput(attrs={'placeholder':'Apartment , Studio, or Floor'}))
        city=forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Toronto,New York'}))
        zip_code=forms.CharField(label='Zip')
        

        
        class Meta:
                model=Contact
                fields=('title','name','sex','email','phone','address1','address2','city','zip_code','company')
        

       