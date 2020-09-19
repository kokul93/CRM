from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views


from . import views
from apps.userprofile import views as profile_view


urlpatterns = [
    path('',views.HomeView.as_view(),name='HomeView'),
    path('register/',views.SignUpView.as_view(),name='register'),
    path('login/',auth_views.LoginView.as_view(
        template_name='common/login.html'
    ),name='login'),
    path('logout/',auth_views.LogoutView.as_view(
        next_page='HomeView'
    ),name='logout'),
    path('dashboard',views.DashboardView.as_view(),name='dashboard'),
    path('change-password/',auth_views.PasswordChangeView.as_view(
            template_name='common/change-password.html',
            success_url='/'
        ),
        name='change-password'
    ),
    #forget password
      # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='common/password-reset/password_reset.html',
             subject_template_name='common/password-reset/password_reset_subject.txt',
             email_template_name='common/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='common/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='common/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='common/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('profile-update/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('company/',profile_view.CompanyListView.as_view(),name='company'),
    path('company/create-company',profile_view.CreateCompanyView.as_view(),name='create_comapany'),
    path('company/<str:pk>',profile_view.CompanyDetailView.as_view(),name='company_detail'),
    path('company/<str:pk>/update/',profile_view.UpdateCompanyView.as_view(),name='company_update'),
    path('company/<str:pk>/delete',profile_view.CompanyDeleteView.as_view(),name='company_delete'),

    path('contacts/',profile_view.ConatactListView.as_view(),name='contacts'),
    path('contacts/create-contact/',profile_view.CreateContact.as_view(),name='create_contact'),
    path('contact/<str:pk>',profile_view.ContactDetailView.as_view(),name='contact_detail'),
    path('contact/<str:pk>/update/',profile_view.UpdateContact.as_view(),name='contact_update'),
    path('contact/<str:pk>/delete',profile_view.ConatactDeleteView.as_view(),name='contact_delete'),

]

