# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.

# class UserAccount(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     email = models.CharField(max_length=255)
#     # address = models.TextField()
#     phone_no = models.IntegerField()
#     personal_document =models.ImageField(upload_to="PersonalDocument/", max_length=1000)
    
#     def _str_(self):
#         return self.name

from django.db import models
from django.contrib.auth.models import User


class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='user_account_mainproject', on_delete=models.CASCADE)
    # other fields and methods

class Employee(models.Model):
    user = models.OneToOneField(User, related_name='user_account_employee', on_delete=models.CASCADE)
    # other fields and methods

class Employee_reg(models.Model):
    euser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    eemail = models.CharField(max_length=255)
    # eaddress = models.TextField()
    epassword = models.CharField(max_length=8)
    ephone_no = models.IntegerField()
    epersonal_document =models.ImageField(upload_to="PersonalDocument/", max_length=1000)
    
    # def _str_(self):
    #     return self.name
    
    class Meta:
        db_table="emp"
        
        
class Emp_login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=8)

    # def _str_(self):
    #     return self.name
    
    class Meta:
        db_table="emp_login"