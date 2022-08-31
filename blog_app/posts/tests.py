from time import time
from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.utils import IntegrityError, DataError

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
    post = Post.objects.get(title = 'my valid title')
    post.user = None
    with self.assertRaises(IntegrityError):
      post.save()

  def test_title_exists(self):
    post = Post.objects.get(title = 'my valid title')
    post.title = None
    with self.assertRaises(IntegrityError):
      post.save()

  def test_title_is_not_empty(self):
    post = Post.objects.get(title = 'my valid title')
    post.title = ''
    with self.assertRaises(ValidationError):
      post.full_clean()

  def test_title_is_not_less_than_5_characters(self):
    post = Post.objects.get(title = 'my valid title')
    post.title = 'four'
    with self.assertRaises(ValidationError):
      post.full_clean()

  def test_title_is_not_greater_than_40_characters(self):
    post = Post.objects.get(title = 'my valid title')
    post.title = 'c ' * 21
    with self.assertRaises(DataError):
      post.save()

  def test_content_exists(self):
    post = Post.objects.get(title = 'my valid title')
    post.content = None
    with self.assertRaises(IntegrityError):
      post.save()

  def test_content_is_not_empty(self):
    post = Post.objects.get(title = 'my valid title')
    post.content = ''
    with self.assertRaises(ValidationError):
      post.full_clean()

  def test_content_is_not_less_than_200_characters(self):
    post = Post.objects.get(title = 'my valid title')
    post.content = 'c'*198
    with self.assertRaises(ValidationError):
      post.full_clean()
