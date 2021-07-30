
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


User.profile = property(
    lambda u: Profile.objects.get_or_create(user=u)[0])


class CrudUser(models.Model):
    first = models.CharField(max_length=30, blank=True)
    last = models.CharField(max_length=100, blank=True)
    short = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    
    contact_number = PhoneNumberField()
    join_date = models.DateTimeField(default=timezone.now)
    image_url = models.URLField(max_length=200)
    medium_url = models.URLField(max_length=200)
    thumbnail_url = models.URLField(max_length=200)
    team = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    last_login = models.DateTimeField(auto_now_add=True)
    loggedIn = models.BooleanField(default=False)

    def __str__(self):
        return self.first

   

