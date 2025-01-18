from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Inventory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cost_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    sales = models.DecimalField(max_digits=10, decimal_places=2)
    stock_date = models.DateField(auto_now=True)
    last_sales_date = models.DateField(auto_now=True)


    def __str__ (self) -> str:
        return f"{self.name} ({self.user.username})"


    def __str__ (self) -> str:
        return f"{self.name} ({self.user.username})"
