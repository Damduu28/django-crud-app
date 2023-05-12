from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

import os

# Create your models here.

def avatar_upload_path(instance, filename):
    upload_to = "profile"
    ext = filename.split('.')[1]
    
    if instance.pk:
        filename = "{}.{}".format(instance.pk, ext)
    else:
        filename = "{}.{}".format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    avatar = models.ImageField(upload_to=avatar_upload_path, default="avatar.png", null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.name if self.name is None else self.username
    
    @property
    def get_first_letter(self):
        try:
            self.name[0]
        except:
            self.username[0]
        
    @property    
    def get_user_name(self):
        try:
            name = self.name
        except:
            name = self.username
            
        return name
    
    @property
    def get_avatar_url(self):
        return self.avatar.url
    
    @property
    def get_total_price(self):
        cruds = self.crud_set.all()
        total = sum([crud.price for crud in cruds])
        return total
    
    
