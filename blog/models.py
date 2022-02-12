from django.db import models
# Create your models here.


class Post(models.Model):
     sn = models.AutoField(primary_key= True)
     title = models.CharField(max_length=500)
     content = models.TextField()
     slug = models.CharField(max_length=500)
     timestamp = models.DateTimeField(blank=True)
     author = models.CharField(max_length=100)

     def __str__(self):
          return self.title + "by" + self.author


