from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=True):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(
            email=email,
            password=password,
            name=name
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    USER_TYPE_CHOICES = [('MEM', 'Member'), ('CCN', 'Course Coordinator'), ('ADM', 'Admin')]
    USER_TYPE_CHOICES1 = [
        ('PSC', 'Primary School Certificate'), ('JSC', 'Junior School Certificate'),
        ('SSC', 'Secondary School Certificate'), ('HSC', 'Higher Secondary Certificate'),
        ('DIP', 'Diploma in Engineering'), ('BSC', 'Bachelor of Science'), ('BA', 'Bachelor of Arts'),
        ('BBA', 'Bachelor of Business Administration'), ('MSC', 'Master of Science'), ('MA', 'Master of Arts'),
        ('MBA', 'Master of Business Administration'), ('PHD', 'Doctor of Philosophy')
    ]

    image = models.ImageField(upload_to='user_image/', blank=True, null=True)
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    name = models.CharField(max_length=50, blank=True)
    education = models.CharField(max_length=20, choices=USER_TYPE_CHOICES1, default='SSC')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    membership_number = models.CharField(max_length=50, unique=True, blank=True, null=True)
    user_type = models.CharField(max_length=8, choices=USER_TYPE_CHOICES, default='MEM')
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email

    def generate_unique_membership_number(self):
        while True:
            membership_number = f'{uuid.uuid4().hex[:8].upper()}'
            if not User.objects.filter(membership_number=membership_number).exists():
                return membership_number

    def save(self, *args, **kwargs):
        if not self.membership_number:
            self.membership_number = self.generate_unique_membership_number()
        super(User, self).save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
