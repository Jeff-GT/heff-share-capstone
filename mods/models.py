from django.db import models

class ModList(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="media/uploads", blank=True, null=True)
    file = models.FileField(upload_to="media/uploads", blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 