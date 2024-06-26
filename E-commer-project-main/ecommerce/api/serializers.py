from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Order
from datetime import datetime

User = get_user_model()
class MMDDYYYYDateField(serializers.Field):
    """
    Serializer field to handle MM-DD-YYYY formatted dates.
    """
    def to_internal_value(self, value):
        try:
            return datetime.strptime(value, '%m-%d-%Y').date()
        except ValueError:
            raise serializers.ValidationError('Invalid date format. Use MM-DD-YYYY.')

    def to_representation(self, value):
        return value.strftime('%m-%d-%Y')

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

class OrderSerializer(serializers.ModelSerializer):
    delivery_date = MMDDYYYYDateField()
    
    class Meta:
        model = Order
        fields = ('id', 'sku', 'name', 'price', 'delivery_date', 'status')
        read_only_fields = ('id', 'status')

