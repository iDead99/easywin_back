from . import models
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    user_id=serializers.IntegerField(read_only=True)
    balance=serializers.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    class Meta:
        model=models.Customer
        fields=['id', 'user_id', 'phone', 'birth_date', 'balance']

class UpdateBalanceSerializer(serializers.ModelSerializer):
    user_id=serializers.IntegerField(read_only=True)
    class Meta:
        model=models.Customer
        fields=['id', 'user_id', 'balance']