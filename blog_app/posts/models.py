from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)  
  content = models.TextField()
  comments_count = models.IntegerField()
  likes_count = models.IntegerField()
  create_date = models.DateField()
  update_date = models.DateField()
