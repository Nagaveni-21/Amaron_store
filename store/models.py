from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

class BatteryStock(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class ServiceReport(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    details = models.TextField()
    date = models.DateField(auto_now_add=True)

class DailyIncome(models.Model):
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
