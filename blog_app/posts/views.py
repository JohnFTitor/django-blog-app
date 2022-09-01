from django.shortcuts import render
from .models import Post

def index(request):
  data = Post.objects.all()
  
  return render(request, 'posts/index.html', context= {
    'data': data
  })
