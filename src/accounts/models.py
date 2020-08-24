from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    _id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
