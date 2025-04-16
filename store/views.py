from django.shortcuts import render, redirect
from .models import BatteryStock, Customer, ServiceReport, DailyIncome
from .forms import CustomerForm, BatteryStockForm, ServiceReportForm, DailyIncomeForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# User Registration
def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirect to login after registration
    else:
        form = RegisterForm()
    return render(request, 'store/register.html', {'form': form})

# User Login
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home after login
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

# User Logout
def logout_user(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# Authentication Views
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'store/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        messages.success(request, 'Account created successfully!')
        return redirect('home')
    
    return render(request, 'store/register.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully logged out!')
    return redirect('login')

# Protected Views
@login_required(login_url='login')
def home(request):
    batteries = BatteryStock.objects.all()
    customers = Customer.objects.all()
    reports = ServiceReport.objects.all()
    daily_income = DailyIncome.objects.all()
    return render(request, 'store/home.html', {'batteries': batteries, 'customers': customers, 'reports': reports, 'daily_income': daily_income})

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Redirect to customer list after saving
    else:
        form = CustomerForm()
    return render(request, 'store/add_customer.html', {'form': form})

@login_required(login_url='login')
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'store/customer_list.html', {'customers': customers})

def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'store/update_customer.html', {'form': form})

def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        customer.delete()
        return redirect('customer_list')
    return render(request, 'store/delete_customer.html', {'customer': customer})

def add_battery(request):
    if request.method == "POST":
        form = BatteryStockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('battery_list')  # Redirect to battery list after saving
    else:
        form = BatteryStockForm()
    return render(request, 'store/add_battery.html', {'form': form})

@login_required(login_url='login')
def battery_list(request):
    batteries = BatteryStock.objects.all()
    return render(request, 'store/battery_list.html', {'batteries': batteries})

def update_battery(request, pk):
    battery = BatteryStock.objects.get(id=pk)
    if request.method == "POST":
        form = BatteryStockForm(request.POST, instance=battery)
        if form.is_valid():
            form.save()
            return redirect('battery_list')
    else:
        form = BatteryStockForm(instance=battery)
    return render(request, 'store/update_battery.html', {'form': form})

def delete_battery(request, pk):
    battery = BatteryStock.objects.get(id=pk)
    if request.method == "POST":
        battery.delete()
        return redirect('battery_list')
    return render(request, 'store/delete_battery.html', {'battery': battery})

def add_service_report(request):
    if request.method == "POST":
        form = ServiceReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_report_list')  # Redirect to service report list after saving
    else:
        form = ServiceReportForm()
    return render(request, 'store/add_service_report.html', {'form': form})

@login_required(login_url='login')
def service_report_list(request):
    reports = ServiceReport.objects.all()
    return render(request, 'store/service_report_list.html', {'reports': reports})

def update_service_report(request, pk):
    report = ServiceReport.objects.get(id=pk)
    if request.method == "POST":
        form = ServiceReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('service_report_list')
    else:
        form = ServiceReportForm(instance=report)
    return render(request, 'store/update_service_report.html', {'form': form})

def delete_service_report(request, pk):
    report = ServiceReport.objects.get(id=pk)
    if request.method == "POST":
        report.delete()
        return redirect('service_report_list')
    return render(request, 'store/delete_service_report.html', {'report': report})

def add_daily_income(request):
    if request.method == "POST":
        form = DailyIncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daily_income_list')  # Redirect after saving
    else:
        form = DailyIncomeForm()
    return render(request, 'store/add_daily_income.html', {'form': form})

@login_required(login_url='login')
def daily_income_list(request):
    incomes = DailyIncome.objects.all()
    return render(request, 'store/daily_income_list.html', {'incomes': incomes})

def update_daily_income(request, pk):
    income = DailyIncome.objects.get(id=pk)
    if request.method == "POST":
        form = DailyIncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('daily_income_list')
    else:
        form = DailyIncomeForm(instance=income)
    return render(request, 'store/update_daily_income.html', {'form': form})

def delete_daily_income(request, pk):
    income = DailyIncome.objects.get(id=pk)
    if request.method == "POST":
        income.delete()
        return redirect('daily_income_list')
    return render(request, 'store/delete_daily_income.html', {'income': income})





