from email.policy import default
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class CustomUserManager(BaseUserManager):
    """This class will manage the interaction between the database and the server."""

    def create_user(self, email, password=None, **other_fields):
        """Custom create user method."""
        if not email:
            raise ValueError("You must provide an email address")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **other_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **other_fields):
        """Create custom superuser method."""
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")

        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")

        return self.create_user(email, password, **other_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model."""

    username = models.CharField(max_length=45, blank=False, null=False, default="John Doe")
    email = models.EmailField(unique=True, blank=False, null=False, max_length=256)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    phone = models.CharField(max_length=25, blank=True)
    location = models.CharField(max_length=128)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, default="/images/test.jpg", null=True, blank=True)
    # theme = models.CharField(max_length=256, blank=True)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self) -> str:
        """String representation for any record from CustomUser table."""
        return self.username

    class Meta:
        """Information about the CustomUser table."""

        verbose_name = "User"
        verbose_name_plural = "Users"
    
