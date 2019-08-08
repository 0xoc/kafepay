from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ProfileCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    class Meta:
        model = UserProfile
        fields = ['username','password','account_number', 'shaba_number']

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
            raise serializers.ValidationError("Useranme Exists")
        except User.DoesNotExist:
            return username

    def create(self, validated_data):
        username = validated_data.pop('username', None)
        password = validated_data.pop('password', None)
        
        user = User(username=username)
        user.set_password(password)
        user.save()

        profile = UserProfile(**validated_data)
        profile.user = user
        profile.save()

        return profile


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'account_number',
            'shaba_number',
            'name',
            'last_name',
            'father_name',
            'meli_number',
            'sh_number',
            'mobile_number',
            'land_number',
            'postal_code',
            'city',
            'address',
            'is_verified', ]
    

    def update(self, instance, validated_data):
        UserProfile.objects.filter(pk=instance().pk).update(**validated_data)
        return instance

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']
    
    def create(self, validated_data):
        p = Product(**validated_data)
        p.profile = self.context.get('profile')

        p.save()

        return p


class GateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gate
        fields = ['title', 'description', 'url']
    
    def create(self, validated_data):
        p = Gate(**validated_data)
        p.profile = self.context.get('profile')

        p.save()

        return p


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'uuid']

class GateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gate
        fields = ['title', 'description', 'url']
