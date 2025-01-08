from rest_framework import serializers
from .models import Account, Destination

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'account_id', 'account_name', 'app_secret_token', 'website']

class DestinationSerializer(serializers.ModelSerializer):
    account_id = serializers.CharField(source='account.account_id')
    class Meta:
        model = Destination
        fields = ['id', 'account_id', 'url', 'http_method', 'headers']
