import email
from rest_framework import serializers
from .models import Todo, UserRegistration
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework.fields import CurrentUserDefault

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"


class TodoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = 'title', 'description'


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRegistration
        fields = ('username', 'email', 'password','linkdin_url','mobile_no','github_url','stack','year_of_experience','languages',
                  'role','profile_picture','price_range','resume_drive_link'
                  )

    def save(self):

        account = UserRegistration(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            profile_picture=self.validated_data['profile_picture'],
            linkdin_url=self.validated_data['linkdin_url'],
            mobile_no=self.validated_data['mobile_no'],
            github_url=self.validated_data['github_url'],
            stack=self.validated_data['stack'],
            year_of_experience=self.validated_data['year_of_experience'],
            languages=self.validated_data['languages'],
            role=self.validated_data['role'],
            price_range=self.validated_data['price_range'],
            resume_drive_link=self.validated_data['resume_drive_link'],
        )
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account


class UpdateRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ('username', 'email', 'password','linkdin_url','mobile_no','linkdin_url','github_url','stack','year_of_experience','languages',
                  'role','profile_picture','price_range','resume_drive_link'
                  )

    def save(self):
        user = self.context.get("request").user
        print(user.email)

        account = UserRegistration.objects.filter(email=user.email)[0]
        account.username = self.validated_data['username']
        account.email = self.validated_data['email']
        password = self.validated_data['password']
        account.linkdin_url = self.validated_data['linkdin_url']
        account.mobile_no = self.validated_data['mobile_no']
        account.linkdin_url = self.validated_data['linkdin_url']
        account.github_url = self.validated_data['github_url']
        account.stack = self.validated_data['stack']
        account.year_of_experience = self.validated_data['year_of_experience']
        account.languages = self.validated_data['languages']
        account.role = self.validated_data['role']
        account.profile_picture = self.validated_data['profile_picture']
        account.price_range = self.validated_data['price_range']
        account.resume_drive_link = self.validated_data['resume_drive_link']


        account.set_password(password)
        account.save()
        return account.password



class RemoveUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRegistration
        fields = ('username', 'email', 'password','linkdin_url','mobile_no','linkdin_url','github_url','stack','year_of_experience','languages',
                  'role','profile_picture','price_range','resume_drive_link'
                  )