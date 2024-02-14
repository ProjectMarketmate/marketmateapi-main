from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import  BaseUserManager

class CustomUser(AbstractUser):
    
     
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_admin = models.BooleanField(default=False)
    mobile = models.CharField(max_length=10)
    image = models.ImageField(upload_to=f'profile/user/',default = 'user.png',blank=True)
    otp = models.IntegerField(null=True,blank=True)
    
    REQUIRED_FIELDS = ['first_name','last_name','mobile','username','is_admin']
    USERNAME_FIELD = 'email'
      
    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ['-date_joined']
        