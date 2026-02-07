from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class movie(models.Model):
    name =models.CharField(max_length=50)
    desc =models.TextField()
    img =models.ImageField ()

    def __str__  (self):
        return self.name

class reviews(models.Model):
    rating=models.IntegerField()
    comment=models.TextField()
    movie_id=models.IntegerField()


from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='profiles/',
        default='profiles/default.png',
        blank=True
    )

    def __str__(self):
        return self.user.username





