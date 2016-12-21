import os
import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(max_length=36, default=uuid.uuid4)

class ListUserManager(BaseUserManager):

    def create_user(self,email):
        ListUser.objects.create(email = email)

    def create_superuser(self,email,password):
        self.create_user(email)



class ListUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(primary_key=True)
#    last_login = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email' 
   # REQUIRED_FIELDS = ['email','height']

    objects = ListUserManager()

    @property
    def is_staff(self):
        return self.email == 'harry.percitval@example.com'
    @property
    def is_ctive(self):
        return True


