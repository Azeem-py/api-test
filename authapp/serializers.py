from wsgiref.validate import validator
from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)
    country = serializers.CharField(required=True,)
    bank = serializers.CharField(required=True, )
    phoneNumber = serializers.IntegerField(required=True)
    accountNumber = serializers.IntegerField(required=True)
    class Meta:
        model = CustomUser

        fields = ('id','username', 'email', 'password', 'password2', 'phoneNumber', 'country', 'bank', 'accountName', 'accountNumber')
        extra_kwargs = {
            'username': {
                'required': True, 
                'validators': [UniqueValidator(CustomUser.objects.all(), "username is not available"),]
            },
            'email':{
                'required': True, 
                'validators': [UniqueValidator(CustomUser.objects.all(), "email is not available"),]
            },
            'email':{
                'required': True, 
                'validators': [UniqueValidator(CustomUser.objects.all(), "email is not available"),]
            },
            'password':{
                'required': True, 'write_only': True,
                'validators': [validate_password,]
            },
            'phoneNumber':{ 
                'validators': [UniqueValidator(CustomUser.objects.all(), "Phone number has used by another user"),]
            },
            'accountNumber':{
                'validators': [UniqueValidator(CustomUser.objects.all(), "Account number has used by another user"),]
            },
        }
        
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields don't match"})
        return attrs

    def create(self, validated_data):
        password, _ = (validated_data.pop('password'), validated_data.pop('password2'))
        newUser = CustomUser.objects.create(**validated_data)
        newUser.set_password(raw_password=password)
        newUser.save()
        return newUser
