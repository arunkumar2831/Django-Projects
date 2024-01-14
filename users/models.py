from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    #creating new table here and below are fields to the tables.
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')
    location=models.CharField(max_length=100)

    #below are used to access the object of this class
    def __str__(self):
        # return f'Profile{self.user.username}'
        return self.user.username
        