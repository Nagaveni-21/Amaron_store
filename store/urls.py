from django.urls import path
from .views import (
    login_view, register_view, logout_view,
    home, customer_list, add_customer, update_customer, delete_customer,
    battery_list, add_battery, update_battery, delete_battery,
    service_report_list, add_service_report, update_service_report, delete_service_report,
    daily_income_list, add_daily_income, update_daily_income, delete_daily_income
)

urlpatterns = [
    # Authentication URLs
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

    # Protected URLs
    path('', home, name='home'),
    path('customers/', customer_list, name='customer_list'),
    path('customers/add/', add_customer, name='add_customer'),
    path('customers/<int:pk>/update/', update_customer, name='update_customer'),
    path('customers/<int:pk>/delete/', delete_customer, name='delete_customer'),

    path('batteries/', battery_list, name='battery_list'),
    path('batteries/add/', add_battery, name='add_battery'),
    path('batteries/<int:pk>/update/', update_battery, name='update_battery'),
    path('batteries/<int:pk>/delete/', delete_battery, name='delete_battery'),

    path('service-reports/', service_report_list, name='service_report_list'),
    path('service-reports/add/', add_service_report, name='add_service_report'),
    path('service-reports/<int:pk>/update/', update_service_report, name='update_service_report'),
    path('service-reports/<int:pk>/delete/', delete_service_report, name='delete_service_report'),

    path('daily-income/', daily_income_list, name='daily_income_list'),
    path('daily-income/add/', add_daily_income, name='add_daily_income'),
    path('daily-income/<int:pk>/update/', update_daily_income, name='update_daily_income'),
    path('daily-income/<int:pk>/delete/', delete_daily_income, name='delete_daily_income'),
]
