from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# registration table
class registration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=models.ImageField()
    phone=models.BigIntegerField()
        
# Coursetype table
class coursetype(models.Model):
    type=models.CharField(max_length=50)

    def __str__(self):
        return self.type

        
# Technology / Categories of Courses
class language(models.Model):
    language=models.CharField(max_length=60)

    def __str__(self):
        return self.language


# Course Table   
class course(models.Model):
    coursetype=models.ForeignKey(coursetype,on_delete=models.CASCADE)
    language=models.ForeignKey(language,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    duration=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField()


# Price table for storing details of paid courses
class price(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    price=models.BigIntegerField()

# subscription table to store subscription details
class subscription(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    durability=models.CharField(max_length=60)
    

# to store payment details
class payment(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.BigIntegerField()
    
# to store cart details
class cart(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
# to store offer details
class offer(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    rate=models.BigIntegerField()
    startdate=models.DateField()
    enddate=models.DateField()

