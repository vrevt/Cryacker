import uuid

from django.db import models
from django.utils import timezone


class Record(models.Model):
    TYPE_CHOICES = (
        ('ETH', 'ethereum'),
        ('BTC', 'bitcoin'),
    )
    id = models.UUIDField(unique=True, default=uuid.uuid4, primary_key=True)
    price = models.DecimalField(decimal_places=18, max_digits=100)
    amount = models.DecimalField(decimal_places=18, max_digits=100)
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.amount > 0:
            plus = '+'
        else:
            plus = ''
        return f"{round(self.price, 1)} {plus}{round(self.amount, 1)} {self.type}"

