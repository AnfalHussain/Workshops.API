from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Workshop,
    Profile,
    Registration,
    Cart)


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        new_user = User(**validated_data)
        new_user.set_password(validated_data['password'])
        new_user.save()
        return validated_data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email"]
        read_only_fields = ['username']


class ProfileUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = "__all__"

    def update(self, instance, validated_data):
        """
        removing (user) key from validated_data dictionary to use update the
        user which has read only username field
        """
        user_field = validated_data.pop('user', None)
        temp_user_serializer = UserSerializer()
        super().update(instance, validated_data)
        super(UserSerializer, temp_user_serializer).update(
            instance.user, user_field)
        return instance


class WorkshopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    carts = CartSerializer(many=True)

    class Meta:
        model = Registration
        fields = '__all__'
