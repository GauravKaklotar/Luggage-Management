from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.CharField(max_length=255)
    address = models.TextField()
    phone_no = models.IntegerField()
    personal_document =models.ImageField(upload_to="PersonalDocument/", max_length=1000)
    
    def __str__(self):
        return self.name
    
    # class Meta:
    #     db_table = "customer"
        
