from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    P_image = models.ImageField(verbose_name='Profile Image',upload_to='prof_image',default='user_default',null=True,blank=True)
    P_user = models.OneToOneField(User,on_delete=models.CASCADE,related_name = 'U_profile')
