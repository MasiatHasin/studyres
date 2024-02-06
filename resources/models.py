from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Resource(models.Model):
    serial_number = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    course = models.CharField(max_length=6)
    semester = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    date= models.DateField(default=timezone.now)
    url = models.URLField(unique=True)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.serial_number} - {self.title} ({self.user.username})"

