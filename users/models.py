from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth.hashers import make_password


def profile_upload_location(instance, filename):
    file_path = 'profile_pictures/{username}-{filename}'.format(
        username=str(instance.username), filename=filename)
    return file_path


def photo_upload_location(instance, filename):
    file_path = 'photos/{username}-{filename}'.format(
        username=str(instance.user.username), filename=filename)
    return file_path

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    REQUIRED_FIELDS = ['email']
    address = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to=profile_upload_location, blank=True)
    following = models.ManyToManyField(
        'self', symmetrical=False, related_name='user_following')
    followers = models.ManyToManyField(
        'self', symmetrical=False, related_name='user_followers')

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to=photo_upload_location)
    likes = models.PositiveIntegerField(default=0)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)


class Hashtag(models.Model):
    hashtag = models.CharField(max_length=50)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='+')
    action = models.CharField(max_length=20)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
