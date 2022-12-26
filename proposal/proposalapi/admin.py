from django.contrib import admin

from .models import Todo,UserRegistration

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'title', 'description', 'datetime']

@admin.register(UserRegistration)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email', 'password','linkdin_url','mobile_no','linkdin_url','github_url','stack','year_of_experience','languages',
                  'role','profile_picture','price_range','resume_drive_link']


from django.contrib import admin

# Register your models here.
