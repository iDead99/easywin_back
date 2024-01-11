from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import action
from . import models
from . import serializers

class CustomerViewSet(ModelViewSet):
    queryset=models.Customer.objects.all()
    serializer_class=serializers.CustomerSerializer
    permission_classes=[permissions.IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        customer=models.Customer.objects.get(user_id=request.user.id)
        if request.method=='GET':
            serializer=serializers.CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method=='PUT':
            serializer=serializers.CustomerSerializer(customer, data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)
        
class UpdateBalanceViewSet(ModelViewSet):
    queryset=models.Customer.objects.all()
    serializer_class=serializers.UpdateBalanceSerializer
    permission_classes=[permissions.IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        customer=models.Customer.objects.get(user_id=request.user.id)
        if request.method=='GET':
            serializer=serializers.UpdateBalanceSerializer(customer)
            return Response(serializer.data)
        elif request.method=='PUT':
            serializer=serializers.UpdateBalanceSerializer(customer, data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)