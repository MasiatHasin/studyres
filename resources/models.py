from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Resource(models.Model):
    sl_no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    course = models.CharField(max_length=6)
    semester = models.CharField(max_length=100, blank = True)
    type = models.CharField(max_length=20)
    date= models.DateField(default=timezone.now)
    url = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.serial_number} - {self.title} ({self.user.username})"

class Upvotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    res_no = models.IntegerField()

