from django.db import models
from django.contrib.auth.models import User

class Resource(models.Model):
    serial_number = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    course = models.CharField(max_length=6)
    type = models.CharField(max_length=20)
    url = models.URLField()
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.serial_number} - {self.title} ({self.user.username})"

