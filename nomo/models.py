from django.db import models

# Create your models here.

# User Model
class User(models.Model):
    name = models.CharField(max_length=100, blank=True)
    dob = models.DateField((""), auto_now=False, auto_now_add=False)
    bio = models.CharField((""), max_length=500)

class Events(models.Model):
    year = models.CharField((""), max_length=100)
    about = models.CharField((""), max_length=300)
    overview_text = models.CharField((""), max_length=100)
    specific_title = models.CharField((""), max_length=100)
    specific_link = models.CharField((""), max_length=100)

class Births(models.Model):
    year = models.CharField((""), max_length=100)
    about = models.CharField((""), max_length=300)
    overview_text = models.CharField((""), max_length=100)
    specific_title = models.CharField((""), max_length=100)
    specific_link = models.CharField((""), max_length=100)

class Deaths(models.Model):
    year = models.CharField((""), max_length=100)
    about = models.CharField((""), max_length=300)
    overview_text = models.CharField((""), max_length=100)
    specific_title = models.CharField((""), max_length=100)
    specific_link = models.CharField((""), max_length=100)

    
def __str__(self):
    return self.name