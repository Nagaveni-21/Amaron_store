from django.contrib import admin
from .models import Customer, BatteryStock, ServiceReport, DailyIncome

admin.site.register(Customer)
admin.site.register(BatteryStock)
admin.site.register(ServiceReport)
admin.site.register(DailyIncome)
