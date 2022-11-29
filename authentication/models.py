from django.db import models
from datetime import datetime
# from django.core.validators import RegexValidator
# Create your models here.

# class user_details(models.Model):
#     first_name = models.CharField(max_length=40)
#     last_name = models.CharField(max_length=40)
#     email_id = models.EmailField()
#     regex_phone_no = RegexValidator(regex="^[0-9]{10}$",message="Phone number must be 10 digit only.")
#     phone_no = models.CharField(validators=[regex_phone_no],max_length=10)
#     username = models.CharField(max_length=6)
#     password = models.pa
#     conf_password

class userInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    bio = models.TextField()
    joined_date = models.DateField(default=datetime.now())
    email_id = models.EmailField()
    is_login = models.BooleanField(default=False)
    def __str__(self):
        return self.username
    
