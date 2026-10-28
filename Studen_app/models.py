from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    course = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __self__(self):
        return self.name