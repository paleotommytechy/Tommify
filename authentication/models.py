from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to="users/", blank=True, default="https://re.cloudinary.com/dhj7zo5li/image/upload/v1744415629/user/profile.png")


    def __str__(self):
        return f"Profile of {self.user.username}"
