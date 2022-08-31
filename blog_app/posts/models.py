from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=40, validators = [MinLengthValidator(limit_value= 5)])  
  content = models.TextField()
  comments_count = models.IntegerField()
  likes_count = models.IntegerField()
  create_date = models.DateField()
  update_date = models.DateField()
