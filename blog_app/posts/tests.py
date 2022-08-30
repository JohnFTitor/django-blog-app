from time import time
from django.test import TestCase
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

class PostModelTests(TestCase):
  def setUp(self):
    user = User.objects.create_user('johnftitor-tester', 'testing@test.com', 'passwurd')
    Post.objects.create(user = user, title = 'my valid title',
    content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse fermentum rutrum feugiat.
    Interdum et malesuada fames ac ante ipsum primis in faucibus. Etiam vitae orci euismod, sagittis elit at,
    porta magna. Donec vel felis placerat, ultricies mauris faucibus, condimentum elit. Proin sit amet elit enim.
    Curabitur ipsum diam, facilisis ut diam eu, aliquet lobortis velit. Cras nec ligula ultricies lacus vestibulum fermentum.
    Curabitur scelerisque vestibulum sem. Cras commodo congue lorem, vel placerat mauris pulvinar vitae. Nulla non enim enim.
    Curabitur vel felis quis massa tincidunt vulputate.""",
    comments_count = 0,
    likes_count = 0,
    create_date = timezone.now(),
    update_date = timezone.now())

  def test_user_exists(self):
    post = Post.objects.get(id= 1)
    post.user = None
    with self.assertRaises(IntegrityError):
      post.save()
