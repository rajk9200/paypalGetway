from django.db import models

class State(models.Model):
    pin = models.CharField(max_length=10)
    name =models.CharField(max_length=20)

    def __str__(self):
        return self.pin
# Create your models here.
class Contacts(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    pincode=models.ForeignKey(State, on_delete=models.CASCADE)
    phone_no=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.name
