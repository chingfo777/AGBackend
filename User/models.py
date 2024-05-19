from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone = models.CharField(max_length=10)

