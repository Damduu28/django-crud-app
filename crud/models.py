from django.db import models
from users.models import User

from uuid import uuid4
import os

# Create your models here.
def image_upload_path(instance, filename):
    upload_to = "profile"
    ext = filename.split('.')[1]
    
    if instance.pk:
        filename = "{}.{}".format(instance.pk, ext)
    else:
        filename = "{}.{}".format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)

class Crud(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=image_upload_path, null=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.title
    
    @property
    def get_crud_image(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url