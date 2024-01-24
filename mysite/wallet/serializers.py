from rest_framework import serializers
from .models import Wallet, Operation
from django.contrib.auth.models import User
 
class WalletSerializer(serializers.Serializer):
    balance_RUB = serializers.FloatField(default=0)
    balance_USD = serializers.FloatField(default=0)
    id_person = serializers.IntegerField()

    def create(self, validated_data):
        return Wallet.objects.create(**validated_data)

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    