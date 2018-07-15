from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User



class input(models.Model):
    event_description = models.TextField(blank=False,null=False) 
    venue =             models.CharField(max_length=50)
    time =              models.TimeField(unique=False)
    date=               models.DateField(blank=True, null=True)
    def __str__(self):
        return  self.event_description

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=True)
    picture = models.ImageField(upload_to="profile_pics",blank=True)

    def __str__(self):
        return self.user.username



