from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    AbstractUser
)
from allbanks.models import(
    Bank
)
from django.utils.translation import gettext_lazy as _
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)        

class CustomUser(AbstractUser):
    username = None
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    acc_number = models.CharField(max_length=10)
    email = models.EmailField(_("email address"), unique=True, blank=False, null=False)
    other_name = models.CharField(max_length=70, blank=True)
    image = models.ImageField(upload_to='images/')
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15, null=False, blank=False, unique=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    account_balance = models.IntegerField(default=0)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class UserTransactions(models.Model):
    TRANSACTION = (
        ("withdraw","withdraw"),
        ("save","save"),  
    )
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    receiver_account_number = models.CharField(max_length=10, null=False,blank=False)
    transaction = models.CharField(max_length=10, choices=TRANSACTION, null=True, blank=True)
    amount = models.IntegerField()

