from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from apps.userprofile.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db import transaction
from .models import *
# Create your views here.


class CompanyListView(LoginRequiredMixin,TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        companys=Company.objects.all()
        user_company=[]
        for company in companys:
            if self.request.user==company.author:
                user_company.append(company)
        context["companys"] =user_company 
        return context
    
    login_url=reverse_lazy('login')



    template_name='common/company/company_list.html'

            

class CompanyDetailView(LoginRequiredMixin,DetailView):
    template_name='common/company/company_detail.html'
    model=Company
    context_object_name='company' 
    ordering=['name']
    login_url=reverse_lazy('login')

class CreateCompanyView(LoginRequiredMixin,CreateView):
    form_class=companyForms
    template_name='common/company/CreateCompany.html'
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    login_url=reverse_lazy('login')

class UpdateCompanyView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Company
    fields=('name','email','phone','address1','address2','city','zip_code','created')
    template_name='common/company/company_update.html'
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        company=self.get_object()
        if self.request.user==company.author:
            return True
        return False

    login_url=reverse_lazy('login')

class CompanyDeleteView(LoginRequiredMixin,DeleteView):
    template_name='common/company/company_delete.html'
    model=Company
    success_url= reverse_lazy('company')

    login_url=reverse_lazy('login')

class ConatactListView(LoginRequiredMixin,TemplateView):
    template_name='common/company/contact_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contacts=Contact.objects.all()
        user_contacts=[]
        for contact in contacts:
            if self.request.user==contact.author:
                user_contacts.append(contact)
        context["contacts"] =user_contacts
        return context
    ordering=['name']

    login_url=reverse_lazy('login')

class CreateContact(LoginRequiredMixin,CreateView):
    form_class=contactForm
    template_name='common/company/create_contact.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    login_url=reverse_lazy('login')


class ContactDetailView(LoginRequiredMixin,DetailView):
    template_name='common/company/contact_detail.html'
    model=Contact
    context_object_name='contact'

    login_url=reverse_lazy('login')

class UpdateContact(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Contact
    fields=fields=('title','name','sex','email','phone','address1','address2','city','zip_code','company')
    template_name='common/company/contact_update.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        contact=self.get_object()
        if self.request.user==contact.author:
            return True
        return False

    
    login_url=reverse_lazy('login')

    

class ConatactDeleteView(LoginRequiredMixin,DeleteView):
    template_name='common/company/contact_delete.html'
    model=Contact
    success_url=reverse_lazy('contacts')

    login_url=reverse_lazy('login')