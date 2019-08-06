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
        fields = ['account_number','shaba_number' ]
    

    def update(self, instance, validated_data):
        account_number = validated_data.pop('account_number', None)
        shaba_number = validated_data.pop('shaba_number', None)

        instance.account_number = account_number
        instance.shaba_number = shaba_number
        
        instance.save()

        return instance
