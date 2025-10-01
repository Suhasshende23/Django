from django.db import models
from decimal import Decimal
# Create your models here.
class Product(models.Model):
    # pk

    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)


    @property
    def sale_price(self):
        return self.price*Decimal("30") #convert into decimal
    
    def get_discount(slef):
        return "122"
    
    

