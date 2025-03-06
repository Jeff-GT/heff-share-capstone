from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="game_images/", null=True, blank=True)
    def __str__(self):
        return self.name

class ModTag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Mod(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.ImageField(upload_to="media/uploads", blank=True, null=True)
    file = models.FileField(upload_to="media/uploads", blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey('Game', on_delete=models.CASCADE, blank=True, null=True)  
    modtags = models.ManyToManyField('ModTag', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.title 
    
class ModImage(models.Model):
    image = models.ImageField(upload_to="mod_images/", null=True, blank=True)
    mod = models.ForeignKey('Mod', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.mod.title + " Image"
    
class Rating(models.Model):
    RATING_TYPES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    ]

    mod = models.ForeignKey('Mod', on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_type = models.CharField(max_length=10, choices=RATING_TYPES)

    def __str__(self):
        return f"{self.user.username} rated with: {self.rating_type} as {self.mod}"











