''' models.py Docstrings'''


from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    ''' models.py class Post Docstrings'''
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        ''' models.py class Post def publish Docstrings'''
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
