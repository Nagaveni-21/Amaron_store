from django import forms
from .models import Customer, BatteryStock, ServiceReport, DailyIncome
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']

class BatteryStockForm(forms.ModelForm):
    class Meta:
        model = BatteryStock
        fields = ['name', 'quantity', 'price']

class ServiceReportForm(forms.ModelForm):
    class Meta:
        model = ServiceReport
        fields = ['customer', 'details']

class DailyIncomeForm(forms.ModelForm):
    class Meta:
        model = DailyIncome
        fields = ['amount']