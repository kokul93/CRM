from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from apps.userprofile.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.
 
class HomeView(TemplateView):
    template_name='common/home.html'

class DashboardView(LoginRequiredMixin,TemplateView):
    template_name='common/Dashboard.html' 
    login_url=reverse_lazy('login')   


class SignUpView(CreateView):
    form_class=SignUpForm
    success_url=reverse_lazy('HomeView')
    template_name='common/register.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name='common/profile.html'
    login_url=reverse_lazy('login')

class ProfileUpdateView(LoginRequiredMixin,TemplateView):
    user_form=UserForm
    profile_form=ProfileForm
    template_name='common/profile-update.html'

    def post(self,request):

        post_data=request.POST or None
        file_data=request.FILES or None

        user_form=UserForm(post_data,instance=request.user)
        profile_form=ProfileForm(post_data,file_data,instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!!!')
            return HttpResponseRedirect(reverse_lazy('profile'))
        
        context=self.get_context_data(
            user_form=user_form,
            profile_form=profile_form
        )
        return self.render_to_response(context)

    def get(self,request,*agrs,**kwargs):
        return self.post(request,*agrs,**kwargs)
    
    login_url=reverse_lazy('login')