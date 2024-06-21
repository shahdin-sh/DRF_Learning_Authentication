from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            "password": {"write_only": True}
        }
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        # check passwords matching and validation
        if password != password2:
            raise serializers.ValidationError({"Error": "Password does not match"})
        
        validate_password(password)

        return attrs
    
    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user = User(username=username, email=email, password=password)

        # use set_password to hash the password correctly
        user.set_password(validated_data['password'])
        user.save()

        return user