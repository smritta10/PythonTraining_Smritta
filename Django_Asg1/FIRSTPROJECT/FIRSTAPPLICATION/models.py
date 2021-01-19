from django.db import models

# Create your models here.

class student(models.Model):
    name= models.CharField(max_length=20)
    S_id= models.IntegerField()
    email= models.EmailField(max_length=15)

    def __str__(self):
        return self.name

class college(models.Model):
    C_name= models.CharField(max_length=20)
    course= models.CharField(max_length=30)

    def __str__(self):
        return self.C_name

class marks(models.Model):
    mark= models.IntegerField()
    course= models.CharField(max_length=30)

    def __str__(self):
        return self.course

