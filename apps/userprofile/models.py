from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(max_length=500,blank=True)
    contact_number=models.CharField(max_length=12,blank=True)
    birth_date=models.DateField(null=True,blank=True)
    profile_image=models.ImageField(default='default-avatar.png',upload_to='users/',null=True,blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()

class Company(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=50)
    address1=models.CharField(max_length=200)
    address2=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zip_code=models.CharField(max_length=50)
    created=models.DateField(default=timezone.now)
    registered=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Companies'

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("company_detail", kwargs={"pk": self.pk})
    
    

class Contact(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    sexChoise=(('Male','male'),('Female','female'))
    titleChoise=(('Mr','mr'),('Mrs','mrs'),('Miss','miss'))
    title=models.CharField(max_length=10,choices=titleChoise)
    name=models.CharField(max_length=200)
    sex=models.CharField(max_length=10,choices=sexChoise)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=50)
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    address1=models.CharField(max_length=200)
    address2=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zip_code=models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("contact_detail", kwargs={"pk": self.pk})