import email
from rest_framework import serializers
from .models import Todo, UserRegistration
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"


class TodoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = 'title', 'description'


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(
        queryset=UserRegistration.objects.all())])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = UserRegistration
        fields = ('username', 'email', 'password', 'password2','linkdin_url','mobile_no','linkdin_url','github_url','stack','year_of_experience','languages',
                  'role','profile_picture','price_range','resume_drive_link'
                  )

    def save(self):
        account = UserRegistration(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        account.set_password(password)
        account.save()
        return account
