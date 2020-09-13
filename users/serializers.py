from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('email','username','password','is_student','is_teacher')


class CustomRegisterSerializer(serializers.ModelSerializer):
    is_student=serializers.BooleanField()
    is_teacher=serializers.BooleanField()

    class Meta:
        model = User
        fields=('email','username','password','is_student','is_teacher')
        extra_kwargs = {'password': {'write_only': True, 'required':True}}

    def validate(self, data):
        if data['is_student'] and data['is_teacher']:
            raise serializers.ValidationError("Cannot be both teacher and student")
        elif not data['is_student'] and not data['is_teacher']:
            raise serializers.ValidationError("should select one")

        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'email':"this email already exists"})

        return data

    @staticmethod
    def validate_username(username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("this username already exists")
        return username

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginS(serializers.Serializer):
    username=serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)


