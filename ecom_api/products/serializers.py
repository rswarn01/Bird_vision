from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User


# Product table serializer to convert data from un-readable to redable
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ["username", "password"]
