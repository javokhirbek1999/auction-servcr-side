from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

# User Manager
class UserManager(BaseUserManager):

    """
    User Manager
    """

    use_in_migrations = True

    def create_user(self, email, user_name, password=None, **extra_fields):

        """Create new user"""

        # Email validation
        if not email:
            raise ValueError(_('Email is required, please enter your email'))

        user = self.model(email=self.normalize_email(email), user_name=user_name, **extra_fields)

        # Sets the given password
        user.set_password(password)

        # Save the user to the database
        user.save(using=self._db)

        return user

    
    def create_superuser(self, email, user_name, password):
        """Create and save a new admin user"""

        user = self.create_user(email=email, user_name=user_name, password=password)

        user.is_active = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


# User Model
class User(AbstractBaseUser, PermissionsMixin):

    """
    Custom User Model
    """

    email = models.EmailField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200, null=False, blank=False, default='')
    last_name = models.CharField(max_length=200, unique=False, blank=False, default='')
    user_name = models.CharField(max_length=200, unique=True, null=True, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['user_name','first_name','last_name']



