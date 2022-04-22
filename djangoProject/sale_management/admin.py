from django.contrib import admin

from .models import Employee, Customer, Product, Order, OrderDetail


admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetail)
