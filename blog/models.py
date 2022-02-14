from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.utils.timezone import now


class Post(models.Model):
     sn = models.AutoField(primary_key= True)
     title = models.CharField(max_length=500)
     content = models.TextField()
     slug = models.CharField(max_length=500)
     timestamp = models.DateTimeField(blank=True)
     author = models.CharField(max_length=100)

     def __str__(self):
          return self.title + "by" + self.author


class Blogcomment(models.Model):
     sno = models.AutoField(primary_key=True)
     comment = models.TextField()
     user = models.ForeignKey(User, on_delete= models.CASCADE)
     post = models.ForeignKey(Post, on_delete= models.CASCADE)
     parent = models.ForeignKey("self",null=True, on_delete= models.CASCADE, )
     timestamp = models.DateTimeField(default = now)