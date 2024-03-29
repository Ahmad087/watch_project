from django.db import models
from shop.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator
from vouchers.models import Voucher

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100, default='Dublin')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class meta:
        ordering = ('-created',)

        def __str__(self):
            return 'Order {}'.format(self.id)

        def get_total_cost(self):
            return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items',
                            on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items',
                            on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    voucher = models.ForeignKey(Voucher, 
                                related_name='orders',
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0,
                            validators=[MinValueValidator(0),
                            MaxValueValidator(100)])
    def __str__(self):
            return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity



