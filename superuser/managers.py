from django.contrib.auth.models import UserManager as BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager): # Here
   
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        extra_fields['username'] = email # username should be as email
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.pswd_token = password
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)