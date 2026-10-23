from django.db import models

class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

 