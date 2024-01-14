from django.db import models
from django.conf import settings
from django.contrib import admin

class Customer(models.Model):
    phone=models.CharField(max_length=255)
    birth_date=models.DateField(null=True, blank=True)
    balance=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    check_box=models.CharField(max_length=10, default='unchecked')

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__last_name')
    def first_name(self):
        return self.user.first_name
    
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    class Meta:

        ordering=['user__first_name', 'user__last_name']
