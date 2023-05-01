from django.db import models
from django.contrib.auth.models import UserManager, PermissionsMixin, AbstractBaseUser
from django.utils import timezone

# Create your models here.

class CustomUserManager(UserManager):
    def _create_user(self, email, name, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('photo', 'default.jpeg')
        return self._create_user(email, name, password, **extra_fields)
    
    def create_superuser(self, email=None, name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('photo', 'default.jpeg')
        return self._create_user(email, name, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    ID = models.AutoField(primary_key=True)
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=255, blank=True, null=True, default='')
    photo = models.ImageField(upload_to="user/", default='default.jpeg', blank=True, null=True)

    server_list_json = models.CharField(max_length=300, default='''{"server-list": [1]}''')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]