from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,

)
# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, unique=True)
    phone_number = models.IntegerField()


class DayOff(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    day_not_avaliable = models.DateField()
