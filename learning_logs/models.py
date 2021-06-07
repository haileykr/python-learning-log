from django.db import models
from django.contrib.auth.models import User

# Model tells  Django how to work with the data which will  be stored in the app
# has attributes and methods like a class
class Topic(models.Model): 
    """A topic the user is learning"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE )

    def __str__(self):
        return self.text #string representation of the model


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'


    def __str__(self):
        return f"{self.text[:50]}..."
        
