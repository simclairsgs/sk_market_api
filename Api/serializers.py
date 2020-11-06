from rest_framework import serializers
from .models import Products,Login,Sales,Stock,Billing,Tax


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields='__all__'

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sales
        fields='__all__'


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stock
        fields='__all__'


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Billing
        fields='__all__'

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tax
        fields='__all__'