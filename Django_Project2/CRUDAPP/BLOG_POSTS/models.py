from django.db import models

# Create your models here.

class blog_model(models.Model):
    blog_name= models.CharField(max_length=100)
    blog_author= models.CharField(max_length=100)

    def __str__(self):
        return self.blog_name



