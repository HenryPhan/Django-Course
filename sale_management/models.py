from django.db import models

# Create your models here.


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    dob = models.DateField(null=True)  # date of birth

    def __str__(self):
        return f'{self.id} - {self.name}'


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    contact_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.phone}'

    def save_name(self):
        self.name = self.name.upper()
        self.save()


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.name}'


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField()
    delivery_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.id} - {self.customer} - {self.employee}'


class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.order} - {self.product}'
