from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_image =  models.ImageField(
        upload_to='profile_images/',
        verbose_name ="Фотография пользователя"
    )
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name ="пользователь"
        verbose_name_plural= "Пользователи"