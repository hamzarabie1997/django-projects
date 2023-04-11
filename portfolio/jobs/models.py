from django.db import models


# Create your models here.
class Jobs(models.Model):
    title = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title