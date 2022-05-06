from django.db import models
from django.contrib.auth.models import User


class CreatedAbstractModel(models.Model):
    created_by = models.ForeignKey(
        User,
        blank=True, null=True, on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_created_by'
    )
    created_at = models.DateTimeField(
        blank=True, null=True, auto_now_add=True,
        db_index=True
    )

    class Meta:
        abstract = True


class ModifiedAbstractModel(models.Model):
    modified_by = models.ForeignKey(
        User,
        blank=True, null=True, on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_modified_by'
    )
    modified_at = models.DateTimeField(
        blank=True, null=True, auto_now=True,
        db_index=True
    )

    class Meta:
        abstract = True


class TrackingAbstractModel(CreatedAbstractModel, ModifiedAbstractModel):
    class Meta:
        abstract = True


class Employee(TrackingAbstractModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    dob = models.DateField(null=True)  # date of birth

    def __str__(self):
        return f'{self.id} - {self.name}'


class Customer(TrackingAbstractModel):
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


class Product(TrackingAbstractModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.name}'


class Order(TrackingAbstractModel):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField()
    delivery_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.id} - {self.customer} - {self.employee}'


class OrderDetail(TrackingAbstractModel):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.order} - {self.product}'

    @property
    def subtotal(self):
        return self.quantity * self.price
