from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=40, validators = [MinLengthValidator(limit_value= 5)])  
  content = models.TextField(validators = [MinLengthValidator(limit_value= 200)])
  comments_count = models.IntegerField(default=0)
  likes_count = models.IntegerField(default= 0)
  create_date = models.DateField()
  update_date = models.DateField()

  def __str__(self):
    return f"{self.title} by {self.user.username}"
