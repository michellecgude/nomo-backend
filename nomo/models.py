from django.db import models

# Create your models here.

# User Model
class User(models.Model):
    name = models.CharField(max_length=100, blank=True)
    dob = models.DateField((""), auto_now=False, auto_now_add=False)
    bio = models.CharField((""), max_length=500)


# Timecapsule Model





# API Model








def __str__(self):
    return self.name