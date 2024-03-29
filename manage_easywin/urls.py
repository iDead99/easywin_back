from rest_framework import routers
from django.urls import path, include
from .import views

router = routers.DefaultRouter()
router.register('customers', views.CustomerViewSet, basename='customer')
router.register('update-balance', views.UpdateBalanceViewSet, basename='update-balance')
router.register('checkbox', views.CheckBoxViewSet, basename='checkbox')
urlpatterns=router.urls