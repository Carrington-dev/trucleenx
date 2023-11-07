from django.db import models
from book.utils import new_payment_id
from book.variables import TIMES



class Order(models.Model):
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=30)
    email           = models.EmailField(max_length=30)
    city            = models.CharField(max_length=300, blank=True, null=True)
    appointed_date  = models.DateTimeField(blank=True, null=True)
    from_time       = models.CharField(max_length=30, choices=TIMES, blank=True, null=True)
    # to_time         = models.CharField(max_length=30, choices=TIMES, blank=True, null=True)
    order_number    = models.CharField(max_length=300, blank=True, null=True)


    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.from_time} {self.order_number} @{self.city}"



    def save(self, *args, **kwargs):  # new
        
        super().save()
        self.order_number = new_payment_id(self.id)
        return super().save(*args, **kwargs)