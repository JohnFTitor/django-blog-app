from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Post


@login_required
def index(request):
  data = Post.objects.all()
  
  return render(request, 'posts/index.html', context= {
    'data': data
  })
