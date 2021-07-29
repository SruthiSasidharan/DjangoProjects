from django.db import models

# Create your models here.
from Guest.models import Library
class Review(models.Model):
    libraryname=models.ForeignKey(Library,on_delete=models.CASCADE)
    review=models.CharField(max_length=250)

    def __str__(self):
        return self.review