from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractUser

from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.



def nameFile(instance, filename):
    print(f"instance:{instance},filename:{filename}")
    return f'images/{filename}'.format(filename=filename)



class UserRegistration(AbstractUser):
    class Roles(models.IntegerChoices):
        """Roles for user model
        """
        ADMIN = 1
        BD = 2
        USER = 3
        MANAGER = 4

    mobile_no = models.CharField(max_length=17, null=True, blank=True, )
    email = models.CharField(
        _('email'),
        max_length=150,
        unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )
    linkdin_url = models.CharField(max_length=1000, blank=True, null=True)
    github_url = models.CharField(max_length=1000, blank=True, null=True)
    stack = models.CharField(max_length=1000, blank=True, null=True)
    year_of_experience = models.CharField(max_length=100, blank=True, null=True)
    languages = models.CharField(max_length=500, blank=True, null=True)
    role = models.PositiveSmallIntegerField(choices=Roles.choices, default=Roles.USER)
    profile_picture = models.ImageField(_('Image'),upload_to=nameFile)
    price_range = models.CharField(max_length=100, blank=True, null=True)
    resume_drive_link = models.CharField(blank=True, max_length=1000, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    objects = CustomUserManager()


from django.db import models

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    datetime = models.DateTimeField(auto_now=True)